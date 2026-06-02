from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import JSONResponse
import random as R

app = FastAPI()

class Item(BaseModel):  
    name: str
    price: float
    is_offer: bool | None = None
   
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return JSONResponse(content={"item_name": item.name, "item_price": item.price, "item_id": item_id})

@app.get("/random/{minimo}/{maximo}")
def funcion(minimo:int,maximo:int):     
    return R.randint(minimo,maximo)

@app.get("/randomb2/")
def funcion(minimo:int,maximo:int):
    if maximo < minimo: 
        raise HTTPException(status_code=400, detail="Sos tonto")     
    return R.randint(minimo,maximo)
    