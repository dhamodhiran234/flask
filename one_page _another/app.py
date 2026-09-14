from flask import Flask,render_template,request
import mysql.connector
from mysql.connector import Error


    # Attempt to connect to the database
dbcon = mysql.connector.connect(
host="localhost",
user="root",
password="Dhamo@123#Db",
database="fla",
auth_plugin="mysql_native_password"  # Add if needed for auth issues
)

if dbcon.is_connected():
    print("Database connection successful!")

# Create cursor only after a successful connection
cursor = dbcon.cursor()
cursor = dbcon.cursor()




app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/Res",methods=['POST'])
def demo():
    if request.method=="POST":
        name=request.form.get("name")
        age=request.form.get("age")
        return render_template("output.html",name=name,age=age)

if (__name__=="__main__"):
    app.run(debug=True)



cursor.close()
dbcon.close()
print("MySQL connection is closed.")