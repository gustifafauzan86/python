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
records = [
	("amel", "amel@gmail.com", 30),
	("igus", "igus@gmail.com", 20),
	("robi", "robi@gmail.com", 40),
	("ari", "ari@gmail.com", 40),
	("rober", "rober@gmail.com", 40),
	("aku", "aku@gmail.com", 40),]

my_cursor.executemany(sqlStuff, records);
konek.commit()