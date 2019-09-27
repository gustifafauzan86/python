#Scrip Melihat database database
import mysql.connector

konek = mysql.connector.connect(
	host = "localhost",
	port = "3307",
	user = "root",
	password = "640078Talu",
	)

my_cursor = konek.cursor()
my_cursor.execute("SHOW DATABASES")

for db in my_cursor:
	print(db)