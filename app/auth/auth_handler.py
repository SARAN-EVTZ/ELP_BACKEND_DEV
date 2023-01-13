import time
from typing import Dict, List

import jwt
from decouple import config

from app.core.config import JWT_ALGORITHM, JWT_SECRET


def token_response(token: str):
    return {"access_token": token}


def signJWT(user_id: str, groups: List) -> Dict[str, str]:
    payload = {
        "email": user_id,
        "groups": groups,  # 1.[admin, ops] 2. [permanennt]
        "expires": time.time() + 600,
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token_response(token)


def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(
            token, JWT_SECRET, algorithms=[JWT_ALGORITHM]
        )
        return (
            decoded_token if decoded_token["expires"] >= time.time() else None
        )
    except Exception:
        return {}
