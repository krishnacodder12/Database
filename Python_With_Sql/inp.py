import mysql.connector as ms

mydb = ms.connect(host="localhost", user="root", password="Krishna@123", database="school")

mycur = mydb.cursor()

mycur.execute("INSERT INTO staff(id int, name varchar(50), role int, sal int )VALUES(1,"KRISHNA", "VICE PRESIDENT" 50000)")
print("Jay Ho")

id = input("Enter Your id:")
name = input("Enter your name:")
role = input("Enter your place on that")
sal = input("Enter your salary package")

