#!C:\Users\welcome\AppData\Local\Programs\Python\Python39\python
import cgi 
import mysql.connector

print("content-type: text/html")
print()
request=cgi.FieldStorage()
f=request.getvalue("mname")

con=mysql.connector.connect(host='localhost',user='root',password='Bhushan@123',database='python')
curs=con.cursor()

try:

    curs.execute("insert into extra values('%s');" %(f))
    con.commit()
    print("<h3>User Registration Successful</h3>")
    print("<html>")
    print("<head>")
    print("<meta http-equiv='refresh' content='0;url=Index.html'/>")
    print("</head>")
    print("</html>")
except :
    
    print("<h3><center>Mobile not Added..<center></h3>")    
    
    print("<br><br><a href='index.html'>Home</a>")