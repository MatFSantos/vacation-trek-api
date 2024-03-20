from datetime import datetime, timedelta
from jose import jwt
from app.config.settings import getSettings
from fastapi.exceptions import HTTPException

def generate(data: dict) -> str:
    settings = getSettings()
    cp = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.EXPIRES_TOKEN)

    cp.update({'exp': expire})

    token = jwt.encode(cp, settings.SECRET_KEY, algorithm=settings.ALGORITHM_TOKEN)
    return token

def verify(token: str) -> dict:
    settings = getSettings()
    payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM_TOKEN])
    return payload