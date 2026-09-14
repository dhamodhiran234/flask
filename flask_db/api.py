from fastapi import FastAPI
import uvicorn
from database import retrieve,conn
from pydantic import BaseModel

app=FastAPI()

class stu(BaseModel):
    name:str
    age:int

@app.get("/")
def home():
    return {"hello":"world"}

@app.get("/getapp")
def index():
    db=conn()
    con=db.cursor(dictionary=True)
    con.execute("select * from stu")   
    row=con.fetchall()
    print(row)
    con.close()
    db.close()
    return row

@app.post("/postapp")
def demo(student:stu):
    db=conn()
    con=db.cursor()
    sql="insert into stu(name,age) values(%s,%s)"
    val=(student.name,student.age)
    con.execute(sql,val)
    db.commit()
    con.close()
    db.close()
    return {
        "data":"successfully inserted",
        "name":student.name,
        "age":student.age
    }


