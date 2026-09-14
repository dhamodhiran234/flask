import mysql.connector

def conn():
    dbcon=mysql.connector.connect(
        host="localhost",
        user="root",
        password="Dhamo@123#Db",
        database="fla",
        auth_plugin="mysql_native_password"
    )
    return dbcon

def retrieve():
    db=conn()
    con=db.cursor()
    sql="select * from stu"
    con.execute(sql)
    rew=con.fetchall()

    
    print(rew)
    con.close()
    db.close()
    return rew

retrieve()
