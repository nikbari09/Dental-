from sqlconnection_dental import *
dbCursor =myDB.cursor()
dbCursor.execute("CREATE TABLE patient(no int(11) AUTO_INCREMENT PRIMARY KEY,name VARCHAR(30), bod date, gender VARCHAR(10), married_status VARCHAR(10), mobile_no VARCHAR(10), whatsapp_no VARCHAR(10), age int(11), address VARCHAR(30), city VARCHAR(10), schedule_date date, time VARCHAR(10))")
print("TABLE IS CREATED!")


