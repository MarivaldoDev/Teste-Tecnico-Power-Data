from fastapi import Header, HTTPException, status
from decouple import config

API_KEY = config("API_KEY").strip().strip('"').strip("'")


def verify_api_key(api_key: str = Header(..., alias="X-API-Key")):
    cleaned_key = api_key.strip().strip('"').strip("'")

    if cleaned_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key"
        )

    return cleaned_key
