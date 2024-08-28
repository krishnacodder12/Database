
import mysql.connector as ms #module aliasing

#using the created database
mydb = ms.connect(host="localhost",user="root",password="Krishna@123",database="HOSPITAL")

#object - cursor
mycur = mydb.cursor()

mycur.execute("CREATE TABLE Doctors(did int,name varchar(30),designation varchar(30),sal int)")
#print("table success")

mycur.execute("SHOW TABLES")

for i in mycur:
    print(i)


