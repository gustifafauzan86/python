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
my_cursor.execute("SELECT * FROM users WHERE age < 30")

result = my_cursor.fetchall()
for data in result:
	print(data[0])