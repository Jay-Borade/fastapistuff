from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def index():
    return {"data":"blog list"}

@app.get("/blog/unpublished")
def unplublished_blogs():
    return {"data":"list of unpublished blogs"}

@app.get("/blog/display")
def display_blogs(limit : int= 10 , published : bool= True, sort : Optional[str]= None):
    if published:
        return {"data":f'{limit} published blogs from the database'}
    else:
        return {"data":f'{limit} blogs from the database'}

@app.get("/blog/{id}")
def show_blog(id : int):
    return {"data":id}


@app.get("/blog/{id}/comment")
def blog_comment():
    return {"data":{'1','2'}}


class Blogs(BaseModel):
    title : str
    body : str
    published : Optional[bool]
    

@app.post("/blog")
def create_post(request:Blogs):
    return {"data":f"Blog is created with the title as {request.title}"}
