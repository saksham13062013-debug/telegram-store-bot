"""
User Model
"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Float
from app.database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, unique=True, index=True)  # Telegram user ID
    username = Column(String, nullable=True)
    first_name = Column(String)
    last_name = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    email = Column(String, nullable=True)
    balance = Column(Float, default=0.0)
    language = Column(String, default="en")
    is_admin = Column(Integer, default=0)
    is_blocked = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f"<User(user_id={self.user_id}, username={self.username})>"
