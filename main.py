from fastapi import FastAPI
from enum import Enum

app = FastAPI()


class ModelName(str, Enum):
    GPT4o = "GPT4o"
    GPTo1 = "GPTo1"
    GPTo3 = "GPTo3"


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/user/{user_id}")
async def handle_user_id(user_id: int):
    return {"message": f"user id is {user_id}"}


@app.get("/models/{model_name}")
async def handle_model_name(model_name: ModelName):
    if model_name is ModelName.GPT4o:
        return {"message": "4o is the basic model", "model_name": model_name}
    if model_name is ModelName.GPTo1:
        return {"message": "o1 is the resoning model", "model_name": model_name}
    if model_name is ModelName.GPTo3:
        return {"message": "4o is the upgraded reasoning model", "model_name": model_name}

@app.get("/items/{item_id}")
async def handle_items(item_id: int, q: str | None = None):
    if q:
        return {"message": f"item_id is {item_id}", "q_value": q}
    return {"message": f"item_id is {item_id}", "q_value": "q doesn't exsit"}