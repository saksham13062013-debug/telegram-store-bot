"""
Order Model
"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, Text, ForeignKey
from app.database import Base

class Order(Base):
    __tablename__ = "orders"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), index=True)
    order_number = Column(String, unique=True, index=True)
    products = Column(Text)  # JSON string of products
    total_price = Column(Float)
    status = Column(String, default="pending")  # pending, paid, completed, cancelled
    payment_method = Column(String, nullable=True)
    shipping_address = Column(Text, nullable=True)
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f"<Order(id={self.id}, user_id={self.user_id}, status={self.status})>"
