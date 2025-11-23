from sqlalchemy import Column, Integer, String, Float
from app.db import Base


class MenuItem(Base):
    __tablename__ = "menu_item"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    is_active = Column(Integer, default=1)
