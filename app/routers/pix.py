from fastapi import APIRouter, Request

router = APIRouter()


@router.post("/")
async def pix_webhook(request: Request):
    data = await request.json()
    print("Webhook PIX:", data)
    return {"status": "OK"}
