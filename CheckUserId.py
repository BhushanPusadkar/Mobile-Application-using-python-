#!C:\Users\welcome\AppData\Local\Programs\Python\Python39\python
import cgi
import mysql.connector

print("Content-type: text/html")
print()

request=cgi.FieldStorage()
id=request.getvalue("uid")

print("<link rel='stylesheet' href='bootstrap.min.css'>")
print("<div class='container'>")

con=mysql.connector.connect(host='localhost',user='root',password='Bhushan@123',database='python')
curs=con.cursor()
curs.execute("select * from users where userid='%s';" %id)
data=curs.fetchone()

if data:
    print("<span style='color:red'>Sorry! Userid not available</span>")
else:
    print("<span style='color:green'>Congrats! Userid is available</span>")


con.close()