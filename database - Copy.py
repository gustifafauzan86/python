
#Fauzan
import mysql.connector

mydb = mysql.connector.connect(
	host = "localhost",
	port = "3307",
	user = "root",
	passwd = "640078Talu",
	database = "testdb",

	)
#print(mydb)

#Create Cursor Instance
my_cursor = mydb.cursor()

# my_cursor.execute("SHOW DATABASES")
# for db in my_cursor:
# 	print(db[0])

#my_cursor.execute("CREATE TABLE users(name VARCHAR(255), email VARCHAR(255), age INTEGER(10), user_id INTEGER AUTO_INCREMENT PRIMARY KEY)")
my_cursor.execute("SHOW TABLES")
for table in my_cursor:
	print(table[0])



# sqlStuff = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
# record1 = ("Fauzan", "fauzan@gmail.com", 40)

# my_cursor.execute(sqlStuff, record1);
# mydb.commit()