from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from ..models.expense import ExpenseStatus, ExpenseCategory

class ExpenseCreate(BaseModel):
    amount: float
    currency: str
    category: ExpenseCategory
    description: str
    expense_date: datetime
    vendor: Optional[str] = None

class ExpenseUpdate(BaseModel):
    amount: Optional[float] = None
    category: Optional[ExpenseCategory] = None
    description: Optional[str] = None
    expense_date: Optional[datetime] = None
    vendor: Optional[str] = None

class ExpenseResponse(BaseModel):
    id: int
    user_id: int
    company_id: int
    amount: float
    currency: str
    converted_amount: Optional[float]
    category: ExpenseCategory
    description: str
    expense_date: datetime
    receipt_url: Optional[str]
    vendor: Optional[str]
    status: ExpenseStatus
    ai_suggested_category: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
