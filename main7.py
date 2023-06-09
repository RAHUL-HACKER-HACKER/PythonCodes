# select user();
# show databases;


# import mysql.connector as c
# conn = c.connect(
#   host="localhost",
#   user="root",
#   password="7261888792",
#   database="pycharmDatabase"
#
# )
# if conn.is_connected():
#
#   print("connection with data base established")
# else:
#   print("unable to connect to database")





# mycursor = conn.cursor()
#create_db="create database pycharmDatabase"
#mycursor.execute(create_db)
# creat_table="create table python(py_id int primary key ,mod_name varchar(20) not null ,use_module varchar(20) )"
# mycursor.execute(creat_table)

#or
# sql = "INSERT INTO python(py_id,mod_name, use_module) VALUES (%s, %s,%s)"
# val = (1, "numpy","math_oper")
# mycursor.execute(sql, val)

#or
# sql = """INSERT INTO python(py_id,mod_name, use_module) VALUES (2,"pipe","sort_fn")"""
#
# mycursor.execute(sql)


#or
import mysql.connector as c
conn = c.connect(
  host="localhost",
  user="root",
  password="7261888792",
  database="pycharmDatabase"

)
mycursor = conn.cursor()

valu="insert into python values (8,'tkinter2','interface2')"

mycursor.execute(valu)
conn.commit()
