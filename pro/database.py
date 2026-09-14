import mysql.connector

def conn():
    db=mysql.connector.connect(
        host="localhost",
        user="root",
        password="Dhamo@123#Db",
        database="fla",
        auth_plugin="mysql_native_password"
    )
    return db

def ret():
    db=conn()
    con=db.cursor(dictionary=True)
    sql="select * from stu"
    con.execute(sql)
    row=con.fetchall()
    print(row)
    con.close()
    db.close()
ret()
