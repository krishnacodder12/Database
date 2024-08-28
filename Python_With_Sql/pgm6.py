import mysql.connector as ms #module aliasing

#using the created database
mydb = ms.connect(host="localhost",user="root",password="Krishna@123",database="HOSPITAL")

#object - cursor
mycur = mydb.cursor()

mycur.execute("INSERT INTO Doctors(did,name,designation,sal) values (%s,%s,%s,%s)",(1,"Sanjana","Chief Doctor",100000))
# %s is a placeholder for a string
#inserting multiple records
#INSERT INTO DOCTORS(DID,NAME,DESIGN,SAL) VALUES(1,2) ,(1,"VICKY","/....") , (3,".......")

mydb.commit()
print("record inserted")
#inserting or updating : u have to use a commit function


