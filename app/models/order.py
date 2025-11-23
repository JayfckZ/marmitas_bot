from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    status = Column(String, default="PENDING_PAYMENT")
    total = Column(Float, default=0)
    created_at = Column(DateTime, default=datetime.now())

    customer = relationship("Customer")
    items = relationship("OrderItem", back_populates="order")
