"""use http://127.0.0.1:8000/docs or http://127.0.0.1:8000/redoc for auto documentation of this API
1. A simple frequency plotter (A Quick histogram for the given data)
"""
from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn

pi = "3.14"
app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


@app.get("/")                       
def read_root():
    return {"Hello, go to /inp?q=<Number of digits of pi you wanna see> "}

@app.get("/inp")
def take_input(q:Optional[int]=3):
    return float(pi[:q+2])

if __name__ == '__main__':
     uvicorn.run(app)