from flask import Flask,render_template,request
from database import conn

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/Res",methods=['POST'])
def index():
    if request.method=="POST":
        nam=request.form.get("name")
        ag=request.form.get("age")
        db=conn()
        con=db.cursor()
        sql="insert into stu(name,age) values(%s,%s)"
        val=(nam,ag)
        con.execute(sql,val)
        db.commit()
        con.close()
        db.close()
        return render_template("res.html",name=nam,age=ag)



if(__name__=="__main__"):
    app.run(debug=True)