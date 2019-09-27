#Script menghubungkan python dengan database
import mysql.connector

konnek = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "640078Talu",
	port = "3307",
	)

print(konnek)