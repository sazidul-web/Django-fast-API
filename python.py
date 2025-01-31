# projecct create command ---  py -3 -m venv venv
# first api iinstall      ---  pip install fastapi[all]
# local server newar command ---- uvicorn python:app ///// uvicorn + file name + app name
# local server newar command ---- uvicorn python:app --reload ///// uvicorn + file name + app name aita dile api reload nibe.

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, world!"}

@app.get("/post")
async def root_post():
    return {"data":"Hello i am sazidul"}