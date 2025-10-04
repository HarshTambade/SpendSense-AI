from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Enum, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from ..database import Base
import enum

class ExpenseStatus(str, enum.Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"

class ExpenseCategory(str, enum.Enum):
    TRAVEL = "travel"
    MEALS = "meals"
    ACCOMMODATION = "accommodation"
    OFFICE_SUPPLIES = "office_supplies"
    ENTERTAINMENT = "entertainment"
    TRANSPORTATION = "transportation"
    UTILITIES = "utilities"
    SOFTWARE = "software"
    TRAINING = "training"
    OTHER = "other"

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False)
    amount = Column(Float, nullable=False)
    currency = Column(String, nullable=False)
    converted_amount = Column(Float, nullable=True)  # Amount in company currency
    category = Column(Enum(ExpenseCategory), nullable=False)
    description = Column(Text, nullable=False)
    expense_date = Column(DateTime, nullable=False)
    receipt_url = Column(String, nullable=True)
    vendor = Column(String, nullable=True)
    status = Column(Enum(ExpenseStatus), default=ExpenseStatus.PENDING)
    ai_suggested_category = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    user = relationship("User", back_populates="expenses")
    company = relationship("Company", back_populates="expenses")
    approvals = relationship("Approval", back_populates="expense")
    risk_score = relationship("RiskScore", back_populates="expense", uselist=False)
