from fastapi import FastAPI, Body, Depends
from model import PostSchema, UserSchema, UserLoginSchema
from app.auth.jwt_handler import sign_JWT
from app.auth.jwt_bearer import jwt_bearer
import uvicorn

posts = [
  {
    "id": 1,
    "title": "penguins",
    "text": "penguins are a group of birds"
  },
  {
    "id": 2,
    "title": "tigers",
    "text": "tigers are the larget living cat species"
  },
  {
    "id": 3,
    "title": "cats",
    "text": "cats awesome"
  }
]

users = [
  {
    "name": "Michael",
    "email": "Michaelmcribgmail.com",
    "password": "thebestdude"
  }
]

app = FastAPI()

@app.get("/", tags=["test"])
def handler():
  return {"Hello": "World"}

@app.get("/posts", tags=["posts"])
def get_posts():
  return {"data" : posts}

@app.get("/posts/{id}", tags=["post"])
def get_one_post(id: int):
  if id > len(posts):
    return {
      "Error" : "Post with this ID does not exist"
    }
  for post in posts:
    if post["id"] == id: #accessing ID property of the post
      return {
        "data" : post
      }

@app.post("/posts", dependencies=[Depends(jwt_bearer())], tags=["posts"])
def add_post(post : PostSchema):
  post.id = len(posts) + 1 #Autoincrementing post ID
  posts.append(post.dict())

  return {
    "info": "Post added"
  }

@app.post("/users/signup", tags=["users"])
def user_signup(user: UserSchema = Body(default=None)):
  users.append(user.dict())
  return sign_JWT(user.email)

def check_user(data: UserLoginSchema):
  for user in users:
    if user.email == data.email and user.password == data.password:
      return True
    return False

@app.post("users/login", tags=["users"])
def sign_up(user: UserLoginSchema = Body(default=None)):
  if check_user(user):
    return sign_JWT(user.email)
  return {"Invalid login datails"}    