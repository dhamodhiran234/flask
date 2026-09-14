from fastapi import FastAPI
from pydantic import BaseModel
from database import db


class Stu(BaseModel):
    name:str
    age:int
app=FastAPI(title="student management api")

@app.get("/")
def home():
    return {"message": "Welcome to Student Management API. Go to /docs for API documentation."}
@app.post("/api/students")
def add_student(student:Stu):
    sucess= db(student.name,str(student.age))
    return {
        "status":"sucess",
        "message":"student inserted sucessfully",
        "data":student
    }

import mysql.connector


dbcon=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Dhamo@123#Db",
    database="fla"
)
@app.get("/api/stu")
def display(student:Stu):
    cursor=dbcon.cursor()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM stu")
    students = cursor.fetchall()
    
    cursor.close()
    dbcon.close()
    return {"status": "success", "data": students}