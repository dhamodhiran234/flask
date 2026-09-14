from fastapi import FastAPI
from database import retrive,conn,add,upd


app=FastAPI()

@app.get("/")
def home():
    return {"hello this : dhamu":"hello"}

@app.get("/getdata")
def demo():
    f=retrive()


