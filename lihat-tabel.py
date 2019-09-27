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
my_cursor.execute("SHOW TABLES")

for tabel in my_cursor:
	print(tabel[0])