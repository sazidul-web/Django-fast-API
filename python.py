# projecct create command ---  py -3 -m venv venv
# first api iinstall      ---  pip install fastapi[all]
# local server newar command ---- uvicorn python:app ///// uvicorn + file name + app name
# local server newar command ---- uvicorn python:app --reload ///// uvicorn + file name + app name aita dile api reload nibe.

from typing import Optional # for rating api
from fastapi import FastAPI # for get api
from fastapi.params import Body # for post api
from pydantic import BaseModel # for post api validation

app = FastAPI()

class Post(BaseModel):
    title:str
    body:str
    publis:bool = False
    rating: Optional[int]=None


@app.get("/")
async def root():
    return {"message": "Hello, world!"}

@app.get("/post")
async def root_post():
    return {"data":"Hello i am sazidul"}
# post api data print hosse .........................
@app.post("/create")
async def create(payload: dict = Body(...)):
    print(payload)
    return {"title": payload["title"],
            "body": payload["body"],
        }

@app.post("/validation")
async def create(New_post:Post):
    print(New_post.rating)
    return {"data":"new post"
        }

