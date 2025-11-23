from fastapi import APIRouter, Request

router = APIRouter()


@router.post("/")
async def whatsapp_webhook(request: Request):
    data = await request.json()
    print("Mensagem recebida:", data)
    return {"received": True}
