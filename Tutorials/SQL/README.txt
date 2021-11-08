structured query language

install
-m pip install mysql-connector

import
import mysql.connector

connect
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword"
)

mycursor = db.cursor()
mycursor.execute("CREATE DATABASE testdatabase")

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword"
  database = "testdatabase"
)

create a table
mycursor.execute("""CREATE TABLE customers (
		first_name text,
		last_name text,
		email text
	)""")
	
commit to database
mydb.commit()
mydb.close()

snake nokias





print(f"my name is {}")








