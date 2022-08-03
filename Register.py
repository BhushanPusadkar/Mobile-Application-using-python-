#!C:\Users\welcome\AppData\Local\Programs\Python\Python39\python
import cgi
import mysql.connector
print("Content-type: text/html")
print()

request=cgi.FieldStorage()
id=request.getvalue("userid")
ps=request.getvalue("pswd")
cps=request.getvalue("cpswd")
nm=request.getvalue("usernm")
ct=request.getvalue("address")
mo=request.getvalue("mobile")


con=mysql.connector.connect(host='localhost',user='root',password='Bhushan@123',database='python')
curs=con.cursor()

try:
     curs.execute("insert into register values('%s','%s','%s','%s','%s','%s');"%(id,ps,cps,nm,ct,mo))
     con.commit()
     print("<h1 style='color:green'> User Registration Successful </h1>")
except:
        print("<h1 style='color:red'>Registration Failed......</h1>")

con.close()
print("<br><br><a href='index.html'>Home</a>")
