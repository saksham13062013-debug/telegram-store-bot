"""
Product Model
"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from app.database import Base

class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text)
    price = Column(Float)
    original_price = Column(Float, nullable=True)
    stock = Column(Integer, default=0)
    category = Column(String, index=True)
    image_url = Column(String, nullable=True)
    is_active = Column(Integer, default=1)
    rating = Column(Float, default=0.0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f"<Product(id={self.id}, name={self.name}, price={self.price})>"
