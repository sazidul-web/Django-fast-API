# projecct create command ---  py -3 -m venv venv
# first api iinstall      ---  pip install fastapi[all]
# local server newar command ---- uvicorn python:app ///// uvicorn + file name + app name
# local server newar command ---- uvicorn python:app --reload ///// uvicorn + file name + app name aita dile api reload nibe.

from typing import Optional
from urllib import response # for rating api
from fastapi import FastAPI , Response, status, HTTPException  # for get api
from fastapi.params import Body # for post api
from pydantic import BaseModel # for post api validation
from random import randrange # for CARD api

app = FastAPI()

class Post(BaseModel):
    title:str
    body:str
    publis:bool = False
    rating: Optional[int]=None

# jsngo list json   ====CARD
my_list=[{"id":1,"title":"django developer","body":"App developer expart"},{"id":2,"title":"Sazidul zoon","body":"Saziudl app developer"}]
# id find funtionn ===================
def find_post(id):
    for p in my_list:
        if p['id']==id:
            return p

# get fast api   =====CARD
@app.get("/mypost")
async def mypost():
    return {"data": my_list}

# curd post api new id create hoiya data base a sob alada vabe save thake........!
@app.post("/curd",status_code=status.HTTP_201_CREATED)
async def curdpost(post: Post):
    post_dict=post.dict()
    post_dict['id']=randrange(0,100000000)
    my_list.append(post_dict)
    return {"data":post_dict}

# lates post api and path is vary important 
@app.get("/mypost/latest")
def get_latest_post():
    post= my_list[len(my_list)-1]
    return {"data":post}


# get post by id ============================================
@app.get("/mypost/{id}")
def mypost(id: int,response: Response):
    print(type(id))
    Post=find_post(id)
    print(type(id))
    if not mypost:
        HTTPException(status_code=status.HTTP)
    # if mypost:
    #     response.status_code=201
    return {"post_details": Post}

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

