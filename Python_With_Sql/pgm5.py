import mysql.connector as ms #module aliasing

#using the created database
mydb = ms.connect(host="localhost",user="root",password="Krishna@123",database="HOSPITAL")

#object - cursor
mycur = mydb.cursor()

mycur.execute("ALTER TABLE Doctors MODIFY COLUMN did int primary key")