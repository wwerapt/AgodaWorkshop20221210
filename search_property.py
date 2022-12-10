import mysql.connector

print("Search Property")
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="",
  database="agoda"
)
mycursor = mydb.cursor()
filter_type = int(input("Filter Type By 1:Property Name ,2: Property type (1 bhk/2 bhk etc.) 3: Property size range (20 to 30 sqm or 30 to 50 sqm etc.) ,):"))
if filter_type == 1:
    property_name = input("Property Name : ")
    sql = 'SELECT * from property \
        left join user on user.userid = property.userid \
        WHERE property.property_name ="' + property_name + '"'
    mycursor.execute(sql)
    property = mycursor.fetchone()
    print("Property Name , Property type , Property Size")
    print(property[1:4])
elif filter_type == 2:
    property_type = int(input("Property Type (1 : 1bhk , 2 : 2bhk etc.) : "))
    sql = 'SELECT * from property \
        left join user on user.userid = property.userid \
        WHERE property.property_type ="' + property_type + '"'
    mycursor.execute(sql)
    property = mycursor.fetchone()
    print("Property Name , Property type , Property Size")
    print(property[1:4])
elif filter_type == 3:    
    property_size = input("Property Size (sqm.): ")
    sql = 'SELECT * from property \
        left join user on user.userid = property.userid \
        WHERE property.property_size ="' + property_size + '"'
    mycursor.execute(sql)
    property = mycursor.fetchone()
    print("Property Name , Property type , Property Size")
    print(property[1:4])





result = mycursor.fetchone()

# print(result)