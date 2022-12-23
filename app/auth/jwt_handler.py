#File responsible for encoding, decoding, signing, and returning JWT's

import time #For invalidating JWTs upon expiry
import jwt
from decouple import config #Deouple helps to organize settings so that parameters can easily changed and be stored in .env files

JWT_SECRET = config("secret") #config() will point to where "secret" is located in our .env file
JWT_ALGORITHM = config("algorithm")

#Returns the generated JWT
def token_response(token: str):
  return {"access token" : token}

#For signing the JWT string
def sign_JWT(user_id: str):
  payload = {
    "user_id" : user_id,
    "expiry" : time.time() + 500
  }
  token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
  return token_response(token)

def decode_JWT(token: str):
  try:
    decode_token = jwt.decode(token, algorithm=JWT_SECRET)
    return decode_token if decode_token['expires'] >= time.time() else None
  except:
    return {}