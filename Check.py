#!C:\Users\welcome\AppData\Local\Programs\Python\Python39\python
import cgi
import mysql.connector

print("Content-type: text/html")
print()

form=cgi.FieldStorage()
id=form.getvalue("userid")
ps=form.getvalue("pswd")

con=mysql.connector.connect(host='localhost',user='root',password='Bhushan@123',database='python')
curs=con.cursor()

curs.execute("select * from register where userid='%s' and pswd='%s';" %(id,ps))
rec=curs.fetchone()

if rec:
    
    print("<html>")
    print("<head>")
    print("<meta http-equiv='refresh' content='0;url=homepage.html'/>")
    print("</head>")
    print("</html>")
else:
    print("<h2 style='color:red'>Sorry Authentication Failde</h2>")
    print("<br><a href='index.html'>Home</a>")

con.close()
