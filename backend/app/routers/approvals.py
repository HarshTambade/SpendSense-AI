from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime
from ..database import get_db
from ..models.user import User, UserRole
from ..models.expense import Expense, ExpenseStatus
from ..models.approval import Approval, ApprovalStatus
from ..schemas.approval import ApprovalResponse, ApprovalUpdate
from ..routers.users import get_current_user

router = APIRouter(prefix="/approvals", tags=["Approvals"])

@router.get("/pending", response_model=List[dict])
def get_pending_approvals(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get pending approvals for current user"""
    
    approvals = db.query(Approval).filter(
        Approval.approver_id == current_user.id,
        Approval.status == ApprovalStatus.PENDING
    ).all()
    
    result = []
    for approval in approvals:
        expense = db.query(Expense).filter(Expense.id == approval.expense_id).first()
        if expense:
            result.append({
                "approval": approval,
                "expense": expense,
                "submitter": expense.user
            })
    
    return result

@router.put("/{approval_id}", response_model=ApprovalResponse)
def update_approval(
    approval_id: int,
    approval_data: ApprovalUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Approve or reject an expense"""
    
    approval = db.query(Approval).filter(Approval.id == approval_id).first()
    if not approval:
        raise HTTPException(status_code=404, detail="Approval not found")
    
    # Check if current user is the approver or admin
    if approval.approver_id != current_user.id and current_user.role != UserRole.ADMIN:
        raise HTTPException(status_code=403, detail="Access denied")
    
    # Update approval
    approval.status = approval_data.status
    approval.comments = approval_data.comments
    approval.approved_at = datetime.utcnow()
    
    # Update expense status
    expense = db.query(Expense).filter(Expense.id == approval.expense_id).first()
    
    if approval_data.status == ApprovalStatus.REJECTED:
        expense.status = ExpenseStatus.REJECTED
    elif approval_data.status == ApprovalStatus.APPROVED:
        # Check if there are more approval steps
        next_approval = db.query(Approval).filter(
            Approval.expense_id == approval.expense_id,
            Approval.workflow_step > approval.workflow_step,
            Approval.status == ApprovalStatus.PENDING
        ).first()
        
        if not next_approval:
            # No more approvals needed
            expense.status = ExpenseStatus.APPROVED
        # else: expense stays pending for next approval
    
    db.commit()
    db.refresh(approval)
    
    return approval

@router.get("/expense/{expense_id}", response_model=List[ApprovalResponse])
def get_expense_approvals(
    expense_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Get all approvals for an expense"""
    
    expense = db.query(Expense).filter(Expense.id == expense_id).first()
    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")
    
    # Check permissions
    if (current_user.role == UserRole.EMPLOYEE and 
        expense.user_id != current_user.id):
        raise HTTPException(status_code=403, detail="Access denied")
    
    approvals = db.query(Approval).filter(
        Approval.expense_id == expense_id
    ).order_by(Approval.workflow_step).all()
    
    return approvals
