#creating databases

import mysql.connector as ms #module aliasing

mydb = ms.connect(host="localhost",user="root",password="Krishna@123")

#object - cursor
mycur = mydb.cursor()

mycur.execute("CREATE DATABASE HOSPITAL")
print("database created successfully")

