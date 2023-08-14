from typing import Union
import asyncio
from fastapi import FastAPI

# uvicorn server:app

app = FastAPI()

data = {}
vid = {}


# uvicorn server:app --host 0.0.0.0

@app.on_event('startup')
async def init_data():
    print("init call")
    data[1] = 0
    data[2] = None
    vid[0] = 0

    return data


@app.get("/getdata/")
async def get_data():
    print("getdata")
    return data[1]


@app.get("/setdata/{value}")
async def set_data(value: str):
    data[1] = int(value)
    print("setdata")
    return data[1]


# uvicorn main:app --host 0.0.0.0 --port 8000

@app.get("/getdatas/")
def get_data():
    print("getdatas")
    return data[2]


@app.get("/setdatas/{value}")
def set_data(value: str):
    data[2] = value
    print("setdatas")
    return data[2]


@app.get("/getvids/")
def get_data():
    print("getvids")
    return vid[0]


@app.get("/setvids/{value}")
def set_data(value: int):
    vid[0] = value
    print("setvids")
    return vid[0]
