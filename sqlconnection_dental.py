import mysql.connector

myDB=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Appointment"
)

print("Database connected",myDB)

'''dbCursor =myDB.cursor()
dbCursor.execute("CREATE DATABASE Appointment")
print("Database Created")'''
'''dbCursor.execute("SHOW DATABASES")
for i in dbCursor:
    print(i)'''



