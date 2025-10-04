from typing import Dict, List
from sqlalchemy.orm import Session
from ..models.expense import Expense
from ..models.risk_score import RiskScore, RiskLevel
import json
from datetime import datetime, timedelta

class RiskService:
    
    @staticmethod
    def calculate_risk_score(expense: Expense, db: Session) -> Dict:
        """Calculate Smart Risk Score for an expense"""
        risk_factors = []
        score = 0
        
        # Factor 1: Amount threshold (0-30 points)
        if expense.converted_amount:
            if expense.converted_amount > 10000:
                score += 30
                risk_factors.append("High amount (>10000)")
            elif expense.converted_amount > 5000:
                score += 20
                risk_factors.append("Medium-high amount (>5000)")
            elif expense.converted_amount > 1000:
                score += 10
                risk_factors.append("Medium amount (>1000)")
        
        # Factor 2: Duplicate detection (0-25 points)
        duplicate_count = db.query(Expense).filter(
            Expense.user_id == expense.user_id,
            Expense.amount == expense.amount,
            Expense.expense_date == expense.expense_date,
            Expense.id != expense.id
        ).count()
        
        if duplicate_count > 0:
            score += 25
            risk_factors.append(f"Potential duplicate ({duplicate_count} similar expenses)")
        
        # Factor 3: Weekend/Holiday submission (0-15 points)
        if expense.expense_date.weekday() >= 5:  # Saturday or Sunday
            score += 15
            risk_factors.append("Weekend expense")
        
        # Factor 4: Frequency check (0-20 points)
        recent_expenses = db.query(Expense).filter(
            Expense.user_id == expense.user_id,
            Expense.created_at >= datetime.utcnow() - timedelta(days=7)
        ).count()
        
        if recent_expenses > 10:
            score += 20
            risk_factors.append(f"High frequency ({recent_expenses} expenses in 7 days)")
        elif recent_expenses > 5:
            score += 10
            risk_factors.append(f"Medium frequency ({recent_expenses} expenses in 7 days)")
        
        # Factor 5: Missing receipt (0-10 points)
        if not expense.receipt_url:
            score += 10
            risk_factors.append("No receipt uploaded")
        
        # Determine risk level
        if score >= 60:
            risk_level = RiskLevel.HIGH
        elif score >= 30:
            risk_level = RiskLevel.MEDIUM
        else:
            risk_level = RiskLevel.LOW
        
        return {
            "score": min(score, 100),
            "risk_level": risk_level,
            "factors": json.dumps(risk_factors)
        }
    
    @staticmethod
    def get_gamified_message(risk_level: RiskLevel, user_name: str) -> str:
        """Generate gamified compliance message"""
        messages = {
            RiskLevel.LOW: [
                f"🌟 Great job, {user_name}! Your expense looks clean and compliant!",
                f"✨ Perfect! {user_name}, you're a compliance superstar!",
                f"🎯 Excellent work, {user_name}! Keep up the good expense habits!"
            ],
            RiskLevel.MEDIUM: [
                f"⚠️ Hey {user_name}, this expense needs a closer look. Double-check the details!",
                f"🔍 {user_name}, we noticed some flags. Please review your submission.",
                f"💡 {user_name}, consider adding more details to improve compliance!"
            ],
            RiskLevel.HIGH: [
                f"🚨 Hold on, {user_name}! This expense has multiple red flags. Please review carefully.",
                f"⛔ {user_name}, this expense requires immediate attention from your manager.",
                f"🔴 Alert! {user_name}, this expense shows high-risk patterns. Contact finance team."
            ]
        }
        
        import random
        return random.choice(messages.get(risk_level, messages[RiskLevel.LOW]))
