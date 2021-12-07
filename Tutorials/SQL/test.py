modules = ["os", "pandas"]
for module in modules:
    try:
        globals()[module] = __import__(module)
    except:
        os.system(f"py -m pip install {module}")
        print(f"Installing {module}")
##print("All modules installed\n")

def pts(mycursor):
    mycursor.execute("SHOW TABLES")
    print(pandas.DataFrame([x for x in mycursor]).to_string(index=False), end = '\n\n')

def pt(mycursor):
    mycursor.execute(f"SELECT * FROM {table}")
    myresult = mycursor.fetchmany(10)
    header = ["student_id","Name","Subject"]
    print(pandas.DataFrame(myresult, columns=header).to_string(index=False), end = '\n\n')

def eo(sql):
    try:
        mycursor.execute(sql)
        mydb.commit()
        print(mycursor.rowcount, f"record(s) inserted successfully into {table} table")
    except mysql.connector.Error as err:
        print(f"Error while running: {sql}\n{err}")

def em(sql,val):
    try:
        mycursor.executemany(sql,val)
        mydb.commit()
        print(mycursor.rowcount, f"record(s) inserted successfully into {table} table")
    except mysql.connector.Error as err:
        print(f"Error while running: {sql}\n{err}")
try:
    import mysql.connector
except Exception as e:
    print(e)
    os.system("py -m pip install mysql-connector-python")
    os.system("py -m pip install mysql.connector")
    import mysql.connector

user = 'root' #input("Username: ")
password = None
while True:
    try:
        mydb = mysql.connector.connect(
          host="127.0.0.1",
          user=user,
          password='haf071197'#password,
        )
        mycursor = mydb.cursor()
    except mysql.connector.Error as err:
        print(err)
        password = input("Password: ")
        continue
    break


mycursor.execute("SHOW DATABASES")
##pp(mycursor)

database = 'giraffe' #input("Database: ")
mydb = mysql.connector.connect(
          host="localhost",
          user=user,
          password='haf071197',#password,
          database = database
        )
mycursor = mydb.cursor()

global table
table = 'student' #input("Table: ")
pts(mycursor)

sql = "DROP TABLE student"
eo(sql)

sql = (
    "CREATE TABLE student ("
    "  student_id INT AUTO_INCREMENT,"
    "  name VARCHAR(20),"
    "  PRIMARY KEY(student_id)"
    ")")
eo(sql)


sql = "INSERT INTO student (student_id,name) VALUES(001, 'Sykkuno')"
eo(sql)

sql = "INSERT INTO student VALUES(%s,%s)"
val = [(2,"Fuslie"),
       (3,"Rae")]
em(sql,val)

mycursor.execute(f"SELECT * FROM {table}")
myresult = mycursor.fetchmany(10)
header = ["student_id","Name","Subject"]
print(pandas.DataFrame(myresult).to_string(index=False), end = '\n\n')










