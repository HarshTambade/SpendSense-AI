from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from ..models.approval import ApprovalStatus

class ApprovalCreate(BaseModel):
    expense_id: int
    approver_id: int
    workflow_step: int

class ApprovalUpdate(BaseModel):
    status: ApprovalStatus
    comments: Optional[str] = None

class ApprovalResponse(BaseModel):
    id: int
    expense_id: int
    approver_id: int
    workflow_step: int
    status: ApprovalStatus
    comments: Optional[str]
    approved_at: Optional[datetime]
    created_at: datetime

    class Config:
        from_attributes = True
