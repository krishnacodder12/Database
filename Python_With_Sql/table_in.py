import mysql.connector as ms

mydb = ms.connect(host="localhost", user = "root", password= "Krishna@123", database = "STUDENT_MANAGEMENT_SYSTEM")

mycur = mydb.cursor()

mycur.execute("CREATE TABLE STUDENT(StudentId int, FirstName varchar(15), LastName varchar(15), DOB int, CourseEnrolled int)")
 
print("table successfully added")