#Membuat Tabel
import mysql.connector

konek = mysql.connector.connect(
	host = "localhost",
	port = "3307",
	user = "root",
	password = "640078Talu",
	database = "db_python",
	)

my_cursor = konek.cursor()
sqlStuff = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
record1 = ("Alfatih", "alfatih@gmail.com", 40)

my_cursor.execute(sqlStuff, record1);
konek.commit()