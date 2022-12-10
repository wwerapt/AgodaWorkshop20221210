import mysql.connector
print("Add Property")
email = input("Email : ")
property_name = input("Property Name : ")
property_type = int(input("Property Type (1 : 1bhk , 2 : 2bhk etc.) : "))
property_size = float(input("Property Size (sqm.): "))

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="",
  database="agoda"
)

mycursor = mydb.cursor()

mycursor.execute('SELECT userid FROM user  WHERE user.email = "' + email + '"')
userid = mycursor.fetchone()


sql = "INSERT INTO property (property_name, property_type, property_size, userid) VALUES (%s, %s, %s, %s)"
val = (property_name, property_type, property_size, userid[0])
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
