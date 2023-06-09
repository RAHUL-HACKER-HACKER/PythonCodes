# import mysql.connector as c
#
# #mpsdl
# conn=c.connectt(
#   host="172.25.160.1",
#   user="RAHUL KUMAR",
#   password="rahulkr7261888792",
#   databasename="student"
# )
#
# if conn.is_connected():
#   print("connection with data base established")
#
# else:
#   print("unable to connect to database")
#
#
#


#create database using python
import mysql.connector as c
conn = c.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="student"
)
if conn.is_connected():
  print("connection with data base established")
else:
  print("unable to connect to database")

mycursor = conn.cursor()
create_db="show database"
creat_table=("python")
mycursor.execute("SHOW DATABASES")


# for x in mycursor:
#   print(x)
