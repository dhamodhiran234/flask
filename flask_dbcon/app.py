from flask import Flask,render_template,request
import mysql.connector
dbcon=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Dhamo@123#Db",
    database="fla",
    auth_plugin="mysql_native_password"
)
if(dbcon.is_connected()):
    print("database connection successfully")
con=dbcon.cursor()

sql="insert into stu(name,age) values(%s,%s)"
    

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/Res",methods=['POST'])
def home():
    if request.method=="POST":
        name=request.form.get("name")
        age=request.form.get("age")
        val=(name,age)
        con.execute(sql,val)
        dbcon.commit()
       
        return render_template("result.html",name=name,age=age)
if __name__=="__main__":
    app.run(debug=True)
con.close()
dbcon.close()


