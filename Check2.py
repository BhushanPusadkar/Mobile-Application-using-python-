#!C:\Users\welcome\AppData\Local\Programs\Python\Python39\python
import cgi
import mysql.connector

print("Content-type: text/html")
print()

form=cgi.FieldStorage()
id=form.getvalue("uid")
ps=form.getvalue("psw")

con=mysql.connector.connect(host='localhost',user='root',password='Bhushan@123',database='python')
curs=con.cursor()

curs.execute("select * from users where userid='%s' and pswd='%s';" %(id,ps))
rec=curs.fetchone()
print('done')
if rec:
    #print("<h2 style='color:green'>Welcome to python on the server </h2>")
    print("<html>")
    print("<head>")
    print("<meta http-equiv='refresh' content='0;url=homepage.html'/>")
    print("</head>")
    print("</html>")
else:
    print("<h2 style='color:red'>Sorry Authentication Failde</h2>")
    print("<br><a href='index.html'>Home</a>")

con.close()
