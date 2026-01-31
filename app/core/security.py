from fastapi import Header, HTTPException, status

API_KEY = "powerofdata-starwars-2025"

def verify_api_key(authorization: str = Header(...)):
    if authorization != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API Key"
        )
