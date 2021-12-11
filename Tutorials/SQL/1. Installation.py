## imports - install if not in system
modules = ["os", "pandas", "getpass"]
for module in modules:
    try:
        globals()[module] = __import__(module)
    except:
        os.system(f"py -m pip install {module}")
        print(f"Installing {module}")
print("All modules installed\n")





## connecting to server - install if mysql not in system
try:
    import mysql.connector
except Exception as e:
    print(e)
    os.system("py -m pip install mysql-connector-python")
    os.system("py -m pip install mysql.connector")
    import mysql.connector



    
## prompt user for username, password and database
user = input("Username (root): ")
password = getpass.getpass("Password: ")
while True:
    try:
        mydb = mysql.connector.connect(
          host="127.0.0.1",
          user=user,
          password=password
        )
        mycursor = mydb.cursor()
    except mysql.connector.Error as err:
        print(err)
        password = getpass.getpass("Password: ")
        continue
    break

mycursor.execute("SHOW DATABASES")
database = input(f"Database {[i for i in mycursor]}: ")
mydb = mysql.connector.connect(
          host="localhost",
          user=user,
          password='haf071197',#password,
          database = database
        )

mycursor = mydb.cursor()
print(f"Connected to {database}\n")

mycursor.execute("SELECT user FROM mysql.user")
print(f"users:\n{[x for x in mycursor]}\n")

mycursor.execute("SHOW TABLES")
print(f"tables: {[x[0] for x in mycursor]}\n")

table_name = input("Table: ")
mycursor.execute(f"DESC {table_name}")
print(f"headers: {[x[0] for x in mycursor]}")

input()











