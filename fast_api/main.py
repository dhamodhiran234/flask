# from fastapi import FastAPI

# app=FastAPI()

# @app.get("/")
# def one():
#     return {'hello':'this dhamu'}
# @app.get("/login")
# def login():
#     return {'login':'this is login'}

from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class User(BaseModel):
    username:str
    password:str


#http  methods::

# 1.get   get the data 
# 2.post   add new data
# 3.put/patch  update the data
# 4.delete   delete the data

@app.get("/")
def home():
    return{'hello':'this is dhamu'}

@app.get("/login")
def ma(user:User):
    print(f"user name:{user.username}")
    print(f"password:{user.password}")
    return {'message':"login successfully"}  #method not allowed









