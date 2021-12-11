## functions
def show_tables(mycursor):
    mycursor.execute("SHOW TABLES")
    print(pandas.DataFrame([x for x in mycursor]).to_string(index=False), end = '\n\n')

def show_tables_v2(mycursor, table, header = None):
    mycursor.execute(f"SELECT * FROM {table}")
    myresult = mycursor.fetchmany(10)
    print("\n",pandas.DataFrame(myresult, columns = header).to_string(index=False), end = '\n\n')

def show_tables_v3(mycursor, header = None):
    mycursor.execute(sql)
    myresult = mycursor.fetchmany(10)
    print("\n",pandas.DataFrame(myresult, columns = header).to_string(index=False), end = '\n\n')

def execute_one(sql):
    try:
        mycursor.execute(sql)
        mydb.commit()
        print(mycursor.rowcount, f"record(s) inserted successfully into table")
    except mysql.connector.Error as err:
        print(f"Error while running: {sql}\n{err}")

def execute_many(sql,val):
    try:
        mycursor.executemany(sql,val)
        mydb.commit()
        print(mycursor.rowcount, f"record(s) inserted successfully into table")
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
show_tables(mycursor)





## start from a clean slate
sql = "DROP TABLE department_head"
execute_one(sql)
sql = "DROP TABLE employees"
execute_one(sql)
sql = "DROP TABLE company_positions"
execute_one(sql)
sql = "DROP TABLE students"
execute_one(sql)
sql = "DROP TABLE scores"
execute_one(sql)
sql = "DROP TABLE classes"
execute_one(sql)








#### declare data types
##sql = (
##    "CREATE TABLE employees ("
##    "  emp_id INT AUTO_INCREMENT,"
##    "  emp_name VARCHAR(20),"
##    "PRIMARY KEY(emp_id)"
##    ")")
##execute_one(sql)
##
#### insert first row
##sql = "INSERT INTO employees (emp_id,emp_name) VALUES(100, 'Liam')"
##execute_one(sql)
##
#### insert other rows
##sql = "INSERT INTO employees(emp_name) VALUES(%s)"
##val = [("Oliver",),
##       ("Theodore",),
##       ("Declan",),
##       ("Henry",),
##       ("Owen",),
##       ("Finn",)]
##execute_many(sql,val)
##
#### show result
##show_tables_v2(mycursor, table = 'employees', header = ["id","name"])
##
##
### 1:1 relationship - one person is the head of every department
##sql = (
##    "CREATE TABLE department_head ("
##    "  dept_name VARCHAR(20),"
##    "  mgr_id INT,"
##    "PRIMARY KEY(dept_name),"
##    "FOREIGN KEY(mgr_id) REFERENCES employees(emp_id) ON DELETE SET NULL"
##    ")")
##execute_one(sql)
##
##sql = "INSERT INTO department_head (dept_name,mgr_id) VALUES('coding', 100)"
##execute_one(sql)
##
##show_tables_v2(mycursor, table = 'department_head', header = ["dept_name","mgr_id"])
##
##sql = '''
##SELECT department_head.dept_name, employees.emp_name
##FROM employees JOIN department_head
##ON employees.emp_id = department_head.mgr_id'''
##
##show_tables_v3(mycursor, header = ["dept_name","manager in charge"])







####--------------------------------------------------------------------
##sql = (
##    "CREATE TABLE employees ("
##    "  emp_id INT AUTO_INCREMENT,"
##    "  emp_name VARCHAR(20),"
##    "  pos_id INT,"
##    "PRIMARY KEY(emp_id)"
##    ")")
##execute_one(sql)
##
##sql = "INSERT INTO employees (emp_id,emp_name,pos_id) VALUES(100,'Liam',200)"
##execute_one(sql)
##
##
##sql = "INSERT INTO employees(emp_name, pos_id) VALUES(%s,%s)"
##val = [("Oliver",200),
##       ("Theodore",200),
##       ("Declan",200),
##       ("Henry",201),
##       ("Owen",201),
##       ("Finn",201)]
##execute_many(sql,val)
##
##show_tables_v2(mycursor, table = 'employees', header = ["emp_id","emp_name","pos_id"])
##
##
##
##
### 1:M - every person needs a role in the company
##sql = (
##    "CREATE TABLE company_positions ("
##    "  pos_id INT,"
##    "  pos_name VARCHAR(20),"
##    "PRIMARY KEY(pos_id)"
##    ")")
##execute_one(sql)
##
##sql = "INSERT INTO company_positions (pos_id,pos_name) VALUES(200, 'coding')"
##execute_one(sql)
##sql = "INSERT INTO company_positions (pos_id,pos_name) VALUES(201, 'marketing')"
##execute_one(sql)
##
######sql = '''SELECT pos_id FROM employees WHERE pos_id NOT IN (SELECT pos_id FROM company_positions)'''
######show_tables_v3(mycursor)
##
##
##sql = '''
##ALTER TABLE employees
##ADD FOREIGN KEY(pos_id)
##REFERENCES company_positions(pos_id)
##ON DELETE SET NULL'''
##execute_one(sql)
##
##sql = '''
##SET FOREIGN_KEY_CHECKS=0
##'''
##execute_one(sql)
##
##sql = '''
##UPDATE company_positions
##SET pos_name = 'code'
##WHERE pos_id = 200 '''
##execute_one(sql)
##
##
##header = ["dept_name","mgr_id"]
##show_tables_v2(mycursor, table = 'company_positions')
##
##sql = '''
##SELECT company_positions.pos_name, employees.emp_name
##FROM employees JOIN company_positions
##ON employees.pos_id = company_positions.pos_id'''
##
##show_tables_v3(mycursor, header = ["dept_name","employees"])






####--------------------------------------------------------------------
#### M:M every student takes many classes
##table_name = 'students'
##sql = (
##    f"CREATE TABLE {table_name} ("
##    f"  stu_name VARCHAR(20),"
##    "PRIMARY KEY(stu_name)"
##    ")")
##execute_one(sql)
##
##sql = f"INSERT INTO {table_name} VALUES('Liam')"
##execute_one(sql)
##
##
##sql = f"INSERT INTO {table_name}(stu_name) VALUES(%s)"
##val = [("Oliver",),
##       ("Theodore",)]
##execute_many(sql,val)
##
##show_tables_v2(mycursor, table = table_name, header = ['stu_name'])
##
##
##
##table_name = 'classes'
##header = ("subject","exam_date")
##sql = (
##    f"CREATE TABLE {table_name} ("
##    f"  {header[0]} VARCHAR(20),"
##    f"  {header[1]} DATE,"
##    "PRIMARY KEY(subject)"
##    ")")
##execute_one(sql)
##
##
##sql = f"INSERT INTO {table_name} VALUES(%s,%s)"
##val = [('English','2021-12-10'),
##       ('Math','2021-12-13')]
##execute_many(sql,val)
##
##show_tables_v2(mycursor, table = table_name, header = header)
##
##
##
##
##table_name = 'scores'
##header = ("stu_name","subject")
##sql = (
##    f"CREATE TABLE {table_name} ("
##    f"  {header[0]} VARCHAR(20),"
##    f"  {header[1]} VARCHAR(20),"
##    "   score INT,"
##    "PRIMARY KEY(stu_name,subject)"
##    ")")
##execute_one(sql)
##
##sql = '''
##ALTER TABLE scores
##ADD FOREIGN KEY(subject)
##REFERENCES classes(subject)
##ON DELETE CASCADE'''
##execute_one(sql)
##
##sql = '''
##ALTER TABLE scores
##ADD FOREIGN KEY(stu_name)
##REFERENCES students(stu_name)
##ON DELETE CASCADE'''
##execute_one(sql)
##
##sql = f"INSERT INTO {table_name} VALUES(%s,%s,%s)"
##val = [('Liam','English',50),
##       ('Liam','Math',80),
##       ('Oliver','English',40),
##       ('Oliver','Math',55),
##       ('Theodore','English',60),
##       ('Theodore','Math',45)]
##execute_many(sql,val)
##
##show_tables_v2(mycursor, table = table_name, header = (*header,'score'))







sql = "DROP TABLE department_head"
execute_one(sql)
sql = "DROP TABLE employees"
execute_one(sql)
sql = "DROP TABLE company_positions"
execute_one(sql)
sql = "DROP TABLE students"
execute_one(sql)
sql = "DROP TABLE scores"
execute_one(sql)
sql = "DROP TABLE classes"
execute_one(sql)






