import mysql.connector as ms

mydb = ms.connect(host="localhost", user = "root", password= "Krishna@123")

mycur = mydb.cursor()

mycur.execute("CREATE DATABASE STUDENT_MANAGEMENT_SYSTEM")

print("database created successfully")