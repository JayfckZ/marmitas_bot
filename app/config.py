import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///db.sqlite3")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    WHATSAPP_API_KEY = os.getenv("WHATSAPP_API_KEY")
    WHATSAPP_API_TOKEN = os.getenv("WHATSAPP_API_TOKEN")
    PIX_API_KEY = os.getenv("PIX_API_KEY")
