import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    salary: float

@app.get("/")
async def read_root():
    return {"Status": "Server is up and running"}

@app.get("/items/{item_id}")
async def read_item(item_id:int):
    return "The item id is ", item_id

@app.put("/items/{item_id}")
async def update_item(item_id:int, item:Item):
    return f"Updated item {item_id} with name {item.name} and salary {item.salary}"

@app.post("/items/")
async def create_item(item:Item):
    return f"Created item with name {item.name} and salary {item.salary}"

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)