from fastapi import FastAPI
from pydantic import BaseModel
from database import conn
from app import index

app=FastAPI(title="student details")

class stu(BaseModel):
    name:str
    age:int
@app.get("/")
def home():
    db=conn()
    con=db.cursor(dictionary=True)

    sql="select * from stu"
    con.execute(sql)

    row=con.fetchall()
    print(row)
    con.close()
    db.close()
    return row

