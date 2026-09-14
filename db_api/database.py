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

def retrive():
    db=conn()
    con=db.cursor(dictionary=True)

    sql="select * from stu"
    con.execute(sql)

    records=con.fetchall()
    print(records)
    for i in records:
        print(i)

    con.close()
    db.close()
    return records


def add(name,age):
    db=conn()
    con=db.cursor()
    sql="insert into stu(name,age) values(%s,%s)"
    values=(name,age)
    con.execute(sql,values)
    
    db.commit()
    con.close()
    db.close()



def upd(n1,nam):
    db=conn()
    con=db.cursor()
    sql="update stu set name=%s where id=%s"
    val=(nam,n1)
    
    con.execute(sql,val)
    
    db.commit()
    con.close()
    db.close()
upd(26,"jani")
retrive()



    