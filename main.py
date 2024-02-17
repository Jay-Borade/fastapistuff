from fastapi import FastAPI,Query
from enum import Enum
from typing import Optional
from pydantic import BaseModel


app=FastAPI()

@app.get("/", description="This is a get api")
async def getmethod():
    return {"Message":"Hello World"}

@app.post("/")
async def postmethod():
    return {"Message":"Hello from the post app "}

@app.put("/")
async def putmethod():
    return {"Message":"Message from put app"}


@app.get("/item/{item_id}")
async def get_item(item_id:int):
    return {"item_id":item_id}

class FoodEnum(str, Enum):
    fruits="fruits"
    vegetables="vegetables"
    dairy="dairy"
    
@app.get("/foods/{food_name}")
async def get_food(food_name:FoodEnum):
    if food_name==FoodEnum.vegetables:
        return {"food_name":food_name, "Message":"You are Healthy"}
    if food_name==FoodEnum.fruits:
        return {"food_name":food_name, "Message":"You are Healthier"}
    if food_name==FoodEnum.dairy:
        return {"food_name":food_name, "Message":"You are non Vegan"}
    return {"food_name":food_name, "Message" :"I like Apple"}
    
    
item_list_db=[{"item_name":"Apple"},{"item_name":"Mango"},{"item_name":"Banana"}]


@app.get("/items")
async def list_items(skip: int = 0, limit: int = 10):
    return item_list_db[skip:skip+limit]
    
@app.get("/items/{item_id}")
async def get_item(item_id:str,q:str | None=None):
    if q:
        return {"item_id":item_id , "q":q}
    return {"item_id":item_id }
    
    
@app.get("/itemsa/{item_ida}")
async def get_item(item_ida : str, q : str | None = None, short : bool=False):
    item = {"item_ida" : item_ida}
    if q:
        item.update({"q":q})
    if not short:
        item.update(
            {
                "description":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer bibendum."
            }
        )
    return item 


class Item(BaseModel):
    name : str
    description : Optional[str] = None
    price : float
    tax : float | None = None
    
@app.post("/items")
async def create_item(item:Item):
    item_dict = item.model_dump()
    if item.tax:
        price_with_tax = item.price +item.tax
        item_dict.update({"price_with_tax" : price_with_tax})
    return item_dict 

@app.put("/items/{item_id}")
async def put_items(item_id : int , item : Item, q : str | None= None): 
    result= {"item_id":item_id, **item.model_dump()}
    if q:
        result.update({"q":q})
    return result
    
    
@app.get("/itemsqq")
async def read_items(q : str | None = Query(None, max_length=10)):
    results={"items":[{"item_id":"Foo"},{"item_id":"Bar"}]}
    if q:
        results.update({"q":q})
    return results