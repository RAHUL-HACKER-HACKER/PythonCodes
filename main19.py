import mysql.connector as c
import webbrowser

conn = c.connect(user='root', password='7261888792',host='localhost',database = 'empdatabase' )

if conn:
    print("Connected Successful;y")
else:
    print("Not Connected")

select_employee = """ SELECT * FROM Employee"""
cursor=conn.cursor()
cursor.execute(select_employee)
result = cursor.fetchall()

p = []
tbl = '<tr><td>ID</td><td>NAME</td><td>EMAIL</td><td>PHONE_NUMBER</td></tr>'
p.append(tbl)

for row in result:
    a = "<tr><td>%s</td>"%row[0]
    p.append(a)
    b= "<td>%s</td>"%row[1]
    p.append(b)
    c= "<td>%s</td>"%row[2]
    p.append(c)
    d= "<td>%s</td>"%row[3]
    p.append(d)

print(p)

contents = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<meta content="text/html; charset=ISO-8859-1"
http-equiv="content-type">
<title>Python Webbrowser</title>
</head>
<body>
<table>
%s
</table>
</body>
</html>
'''%(p)

filename = 'webbrowser.html'
def main(contents,filename):
    output = open(filename,'w')
    output.write(contents)
    output.close()

main(contents,filename)
webbrowser.open(filename)

if(conn.is_connected()):
    cursor.close()
    conn.close()
    print("Mysql connection is closed")

import os
print(os.getcwd())