import mysql.connector as ms

mydb = ms.connect(host="localhost", user= "root", password="Krishna@123", database ="HOSPITAL")

mycur = mydb.cursor()

mycur.execute("CREATE TABLE Doctors(did int, name varchar(30), designation varchar(55), sal int)")
print("table successfully added")