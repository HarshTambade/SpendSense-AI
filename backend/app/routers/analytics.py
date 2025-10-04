from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func, extract
from typing import List, Dict
from datetime import datetime, timedelta
from ..database import get_db
from ..models.user import User, UserRole
from ..models.expense import Expense, ExpenseCategory, ExpenseStatus
from ..models.risk_score import RiskScore, RiskLevel
from ..routers.users import get_current_user

router = APIRouter(prefix="/analytics", tags=["Analytics"])

@router.get("/dashboard")
def get_dashboard_analytics(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get AI-powered dashboard insights"""
    
    # Get company expenses
    company_expenses = db.query(Expense).filter(
        Expense.company_id == current_user.company_id
    ).all()
    
    # Total spend
    total_spend = sum(e.converted_amount or 0 for e in company_expenses)
    
    # Spend by category
    category_spend = {}
    for expense in company_expenses:
        cat = expense.category.value
        category_spend[cat] = category_spend.get(cat, 0) + (expense.converted_amount or 0)
    
    # Monthly trend (last 6 months)
    six_months_ago = datetime.utcnow() - timedelta(days=180)
    monthly_expenses = db.query(
        extract('month', Expense.expense_date).label('month'),
        func.sum(Expense.converted_amount).label('total')
    ).filter(
        Expense.company_id == current_user.company_id,
        Expense.expense_date >= six_months_ago
    ).group_by('month').all()
    
    monthly_trend = [{"month": m, "total": float(t or 0)} for m, t in monthly_expenses]
    
    # Risk distribution
    risk_distribution = db.query(
        RiskScore.risk_level,
        func.count(RiskScore.id).label('count')
    ).join(Expense).filter(
        Expense.company_id == current_user.company_id
    ).group_by(RiskScore.risk_level).all()
    
    risk_stats = {r.value: c for r, c in risk_distribution}
    
    # Top vendors
    vendor_spend = db.query(
        Expense.vendor,
        func.sum(Expense.converted_amount).label('total')
    ).filter(
        Expense.company_id == current_user.company_id,
        Expense.vendor.isnot(None)
    ).group_by(Expense.vendor).order_by(func.sum(Expense.converted_amount).desc()).limit(5).all()
    
    top_vendors = [{"vendor": v, "total": float(t or 0)} for v, t in vendor_spend]
    
    # Approval stats
    pending_count = db.query(Expense).filter(
        Expense.company_id == current_user.company_id,
        Expense.status == ExpenseStatus.PENDING
    ).count()
    
    approved_count = db.query(Expense).filter(
        Expense.company_id == current_user.company_id,
        Expense.status == ExpenseStatus.APPROVED
    ).count()
    
    rejected_count = db.query(Expense).filter(
        Expense.company_id == current_user.company_id,
        Expense.status == ExpenseStatus.REJECTED
    ).count()
    
    # AI Insights
    insights = []
    
    # Insight 1: Spending forecast
    if len(monthly_trend) >= 3:
        recent_avg = sum(m['total'] for m in monthly_trend[-3:]) / 3
        forecast = recent_avg * 1.1  # Simple 10% growth forecast
        insights.append({
            "type": "forecast",
            "title": "Spending Forecast",
            "message": f"Based on recent trends, projected spend next month: {current_user.company.currency} {forecast:.2f}",
            "value": forecast
        })
    
    # Insight 2: High-risk expenses
    high_risk_count = risk_stats.get(RiskLevel.HIGH.value, 0)
    if high_risk_count > 0:
        insights.append({
            "type": "risk",
            "title": "High-Risk Alert",
            "message": f"{high_risk_count} expenses flagged as high-risk. Review recommended.",
            "value": high_risk_count
        })
    
    # Insight 3: Top spending category
    if category_spend:
        top_category = max(category_spend.items(), key=lambda x: x[1])
        insights.append({
            "type": "category",
            "title": "Top Spending Category",
            "message": f"{top_category[0].replace('_', ' ').title()} accounts for {current_user.company.currency} {top_category[1]:.2f}",
            "value": top_category[1]
        })
    
    # Policy suggestions
    policy_suggestions = []
    
    if high_risk_count > 5:
        policy_suggestions.append({
            "title": "Strengthen Approval Rules",
            "description": "Consider adding additional approval steps for expenses over a certain threshold.",
            "priority": "high"
        })
    
    if category_spend.get('travel', 0) > total_spend * 0.4:
        policy_suggestions.append({
            "title": "Travel Policy Review",
            "description": "Travel expenses are 40%+ of total spend. Review travel policy for optimization.",
            "priority": "medium"
        })
    
    return {
        "total_spend": total_spend,
        "currency": current_user.company.currency,
        "category_spend": category_spend,
        "monthly_trend": monthly_trend,
        "risk_distribution": risk_stats,
        "top_vendors": top_vendors,
        "approval_stats": {
            "pending": pending_count,
            "approved": approved_count,
            "rejected": rejected_count
        },
        "ai_insights": insights,
        "policy_suggestions": policy_suggestions
    }

@router.get("/user-stats")
def get_user_stats(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get user-specific expense statistics"""
    
    user_expenses = db.query(Expense).filter(
        Expense.user_id == current_user.id
    ).all()
    
    total_submitted = len(user_expenses)
    total_amount = sum(e.converted_amount or 0 for e in user_expenses)
    approved = sum(1 for e in user_expenses if e.status == ExpenseStatus.APPROVED)
    rejected = sum(1 for e in user_expenses if e.status == ExpenseStatus.REJECTED)
    pending = sum(1 for e in user_expenses if e.status == ExpenseStatus.PENDING)
    
    return {
        "total_submitted": total_submitted,
        "total_amount": total_amount,
        "approved": approved,
        "rejected": rejected,
        "pending": pending,
        "approval_rate": (approved / total_submitted * 100) if total_submitted > 0 else 0
    }
