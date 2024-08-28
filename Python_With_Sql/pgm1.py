#connecting python with mysql
#LIBRARY - COLLECTION OF MODULES
#MODULE - COLLECTION OF FUNCTIONS
import mysql.connector as ms

mydb = ms.connect(host="Localhost",user="root",password="Krishna@123")

print(mydb)


