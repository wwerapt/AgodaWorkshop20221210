import mysql.connector

print("Please enter information below")
email = input("Email : ")
name = input("Name : ")

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="",
  database="agoda"
)

mycursor = mydb.cursor()

sql = "INSERT INTO user (name, email) VALUES (%s, %s)"
val = (name, email)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
