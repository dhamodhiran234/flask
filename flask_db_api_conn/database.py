
import mysql.connector
def db(n1,n2):
    dbcon=None
    con=None
   

    #connection


    dbcon=mysql.connector.connect(
        host="localhost",
        user="root",
        password="Dhamo@123#Db",
        database="fla"
    )

    if dbcon.is_connected():
        print("database connection successfully::")
        con=dbcon.cursor()
        sql="insert into stu(name,age) values(%s,%s)"
        val=(n1,n2)
        con.execute(sql,val)
        print("data inserted successfully")
        dbcon.commit()
        return True

    con.close()
    dbcon.close()







