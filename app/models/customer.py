from enum import unique

from sqlalchemy import Colum, Integer, String
from app.db import Base


class Customer(Base):
    __tablename__ = "customer"

    id = Column(Integer, primary_key=True, index=True)
    whatsapp = Column(String, unique=True, index=True)
    name = Column(String)
    address = Column(String, nullable=True)
