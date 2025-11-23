from fastapi import APIRouter, Depends
from app.db import SessionLocal
from app.models.order import Order

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def list_order(db=Depends(get_db)):
    return db.query(Order).all()
