#For persisting authentication -- authorizing access of protected routes
from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from .jwt_handler import decode_JWT

class jwt_bearer(HTTPBearer):
  def __init__(self, auto_Error: bool = True):
    super(jwt_bearer, self).__init__(auto_error=auto_Error)
    async def __call__(self, request: Request):
      credentials: HTTPAuthorizationCredentials = await super(jwt_bearer, self).__call__(request)
      if credentials:
        if not credentials.scheme == "Bearer":
          raise HTTPException(status_code=403, details="Invalid or expired token")
        else:
          return credentials.credentials
      else: 
        raise HTTPException(status_code=403, details="Invalid or expired token")

  def verify_jwt(self, jwt_token: str):
    is_valid_token: bool = False
    payload = decode_JWT(jwt_token)
    if payload:
      is_valid_token = True
    return is_valid_token
