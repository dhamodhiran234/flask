from flask import Flask,render_template,request
from database import db


app=Flask(__name__)

@app.route("/")

def home():
    return render_template("index.html")
@app.route("/Res",methods=['POST'])
def index():
    if request.method=='POST':
        name=request.form.get("name")
        age=request.form.get("a")

        f=db(name,age)
        return render_template("output.html",name=name,age=age)

if __name__=="__main__":
    app.run(debug=True)