import mysql.connector as ms

mydb = ms.connect(host="localhost", user = "root", password= "Krishna@123", database = "STUDENT_MANAGEMENT_SYSTEM")

mycur = mydb.cursor()

mycur.execute("INSERT INTO STUDENT(StudentId,FirstName,LastName,DOB,CourseEnrolled) values (%s,%s,%s,%s,%s)",(3105,"Krishna","Kumar",2002, 3))

mydb.commit()
 
print("record inserted inside student")

