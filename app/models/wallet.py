"""
Wallet Model
"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, Text, ForeignKey
from app.database import Base

class Wallet(Base):
    __tablename__ = "wallets"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), unique=True, index=True)
    balance = Column(Float, default=0.0)
    transactions = Column(Text)  # JSON string of transactions
    total_spent = Column(Float, default=0.0)
    total_received = Column(Float, default=0.0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f"<Wallet(user_id={self.user_id}, balance={self.balance})>"
