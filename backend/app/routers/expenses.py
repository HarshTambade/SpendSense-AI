from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime
from ..database import get_db
from ..models.user import User, UserRole
from ..models.expense import Expense, ExpenseStatus, ExpenseCategory
from ..models.approval import Approval, ApprovalStatus
from ..models.risk_score import RiskScore
from ..schemas.expense import ExpenseCreate, ExpenseResponse, ExpenseUpdate
from ..routers.users import get_current_user
from ..services.external_api import ExternalAPIService
from ..services.risk_service import RiskService
import base64
import os

router = APIRouter(prefix="/expenses", tags=["Expenses"])

@router.post("/", response_model=ExpenseResponse)
async def create_expense(
    amount: float = Form(...),
    currency: str = Form(...),
    category: ExpenseCategory = Form(...),
    description: str = Form(...),
    expense_date: str = Form(...),
    vendor: Optional[str] = Form(None),
    receipt: Optional[UploadFile] = File(None),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Create new expense with optional receipt upload"""
    
    # Parse expense date
    try:
        parsed_date = datetime.fromisoformat(expense_date.replace('Z', '+00:00'))
    except:
        parsed_date = datetime.utcnow()
    
    # Get company currency and convert
    company = current_user.company
    converted_amount = ExternalAPIService.convert_currency(
        amount, currency, company.currency
    )
    
    # Handle receipt upload and OCR
    receipt_url = None
    ocr_data = None
    if receipt:
        # Save receipt (in production, use cloud storage)
        receipt_data = await receipt.read()
        receipt_filename = f"receipt_{current_user.id}_{datetime.utcnow().timestamp()}.jpg"
        receipt_path = f"/tmp/{receipt_filename}"
        
        with open(receipt_path, "wb") as f:
            f.write(receipt_data)
        
        receipt_url = receipt_path
        
        # Extract text from receipt using OCR
        ocr_data = await ExternalAPIService.extract_text_from_receipt(receipt_data)
    
    # Get AI category suggestion
    ai_category = await ExternalAPIService.classify_expense_category(description)
    
    # Create expense
    expense = Expense(
        user_id=current_user.id,
        company_id=current_user.company_id,
        amount=amount,
        currency=currency,
        converted_amount=converted_amount,
        category=category,
        description=description,
        expense_date=parsed_date,
        receipt_url=receipt_url,
        vendor=vendor or (ocr_data.get("vendor") if ocr_data else None),
        ai_suggested_category=ai_category,
        status=ExpenseStatus.PENDING
    )
    
    db.add(expense)
    db.commit()
    db.refresh(expense)
    
    # Calculate risk score
    risk_data = RiskService.calculate_risk_score(expense, db)
    risk_score = RiskScore(
        expense_id=expense.id,
        score=risk_data["score"],
        risk_level=risk_data["risk_level"],
        factors=risk_data["factors"]
    )
    db.add(risk_score)
    
    # Create approval workflow (Manager -> Finance -> Director)
    if current_user.manager_id:
        approval = Approval(
            expense_id=expense.id,
            approver_id=current_user.manager_id,
            workflow_step=1
        )
        db.add(approval)
    
    db.commit()
    db.refresh(expense)
    
    return expense

@router.get("/", response_model=List[ExpenseResponse])
def get_expenses(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get expenses based on user role"""
    
    if current_user.role == UserRole.ADMIN:
        # Admin sees all company expenses
        expenses = db.query(Expense).filter(
            Expense.company_id == current_user.company_id
        ).order_by(Expense.created_at.desc()).all()
    elif current_user.role == UserRole.MANAGER:
        # Manager sees team expenses
        subordinate_ids = [u.id for u in current_user.subordinates]
        subordinate_ids.append(current_user.id)
        expenses = db.query(Expense).filter(
            Expense.user_id.in_(subordinate_ids)
        ).order_by(Expense.created_at.desc()).all()
    else:
        # Employee sees own expenses
        expenses = db.query(Expense).filter(
            Expense.user_id == current_user.id
        ).order_by(Expense.created_at.desc()).all()
    
    return expenses

@router.get("/{expense_id}", response_model=ExpenseResponse)
def get_expense(
    expense_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get expense by ID"""
    
    expense = db.query(Expense).filter(Expense.id == expense_id).first()
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    
    # Check permissions
    if current_user.role == UserRole.EMPLOYEE and expense.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Access denied")
    
    return expense

@router.get("/{expense_id}/risk")
def get_expense_risk(
    expense_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get risk score for expense"""
    
    expense = db.query(Expense).filter(Expense.id == expense_id).first()
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    
    risk_score = db.query(RiskScore).filter(RiskScore.expense_id == expense_id).first()
    if not risk_score:
        raise HTTPException(status_code=404, detail="Risk score not found")
    
    # Get gamified message
    gamified_message = RiskService.get_gamified_message(
        risk_score.risk_level,
        current_user.full_name
    )
    
    import json
    return {
        "expense_id": expense_id,
        "score": risk_score.score,
        "risk_level": risk_score.risk_level,
        "factors": json.loads(risk_score.factors),
        "message": gamified_message
    }
