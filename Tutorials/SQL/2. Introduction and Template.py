## functions
def show_tables(mycursor, header = ["table_name"]):
    mycursor.execute("SHOW TABLES")
    print(pandas.DataFrame([x for x in mycursor], columns = header).to_string(index=False), end = '\n\n')

def show_tables_v2(mycursor, header = None):
    mycursor.execute(f"SELECT * FROM {table}")
    myresult = mycursor.fetchmany(10)
    print("\n",pandas.DataFrame(myresult, columns = header).to_string(index=False), end = '\n\n')

def execute_one(sql):
    try:
        mycursor.execute(sql)
        mydb.commit()
        print(mycursor.rowcount, f"record(s) inserted successfully into {table} table")
    except mysql.connector.Error as err:
        print(f"Error while running: {sql}\n{err}")

def execute_many(sql,val):
    try:
        mycursor.executemany(sql,val)
        mydb.commit()
        print(mycursor.rowcount, f"record(s) inserted successfully into {table} table")
    except mysql.connector.Error as err:
        print(f"Error while running: {sql}\n{err}")






        


## connecting to server
import mysql.connector, pandas

user = 'root' 
password = 'haf071197'
database = 'giraffe'

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user=user,
  password=password,
  database = database
)
mycursor = mydb.cursor()

global table
table = 'student'
show_tables(mycursor)










## start from a clean slate
sql = "DROP TABLE student"
execute_one(sql)

## declare table and data types
sql = (
    "CREATE TABLE student ("
    "  student_id INT AUTO_INCREMENT,"
    "  name VARCHAR(20),"
    "PRIMARY KEY(student_id)"
    ")")
execute_one(sql)

## insert first row
sql = "INSERT INTO student (student_id,name) VALUES(100, 'Liam')"
execute_one(sql)

## insert other rows
sql = "INSERT INTO student(name) VALUES(%s)"
val = [("Oliver",),
       ("Theodore",),
       ("Declan",),
       ("Henry",),
       ("Owen",),
       ("Finn",)]
execute_many(sql,val)

## show result
show_tables_v2(mycursor,header = ["student_id","name"])










