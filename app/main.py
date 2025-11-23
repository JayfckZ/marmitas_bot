from fastapi import FastAPI
from app.db import Base, engine
from app.routers import whatsapp, pix, orders

app = FastAPI(title="MarmitaBot API")

Base.metadata.create_all(bind=engine)

app.include_router(orders.router, prefix="/orders", tags=["Orders"])
app.include_router(whatsapp.router, prefix="/webhook/whatsapp", tags=["Whatsapp"])
app.include_router(pix.router, prefix="/webhook/pix", tags=["Pix"])


@app.get("/")
def root():
    return {"status": "OK", "message": "MarmitaBot rodando!"}
