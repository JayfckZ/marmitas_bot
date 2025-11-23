from sqlalchemy import Column, Integer, Float, String, ForeignKey
from app.db import Base


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    txid = Column(String, index=True)
    status = Column(String, default="PENDING")
    value = Column(Float)
