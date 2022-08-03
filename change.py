#!C:\Users\welcome\AppData\Local\Programs\Python\Python39\python 
import cgi
import mysql.connector

print("content-type: text/html")
print()

print("<link rel='stylesheet' href='bootstrap.min.css'>")
print("<style>body{ background-image:url(image/girl.gif); background-size:800px 850px;}fieldset { border-radius:20px; margin-left:360px; border:3px solid black; background-color:skyblue; width:40%; color:black; font-weight:bold; padding:40px; font-size:20px; }</style>")
print("<div class='container'>")
print("<br><br><h2 style='background-color : powderblue; text-align:center; margin-left:390px; width:400px; padding:30px;'>Address is</h2><hr>")


request=cgi.FieldStorage()
m=request.getvalue("search")
c=request.getvalue("adress")

con=mysql.connector.connect(host='localhost',user='root',password='Bhushan@123',database='python')
curs=con.cursor()

try:
    print("<fieldset>")

    curs.execute("update users set address='%s' where usernm='%s'" %(c,m))
    con.commit()
    
    curs.execute("select * from users where usernm='%s'" %m)
    rec=curs.fetchone()
    
    print("<br><br>Address : %s" %rec[4])
    
    print()
    print('<br><br><a href="Index.html">---->back</a>')
    print("<br></fieldset>")

except:
    print("<br><br><br><br>Address not found<br><br><br><br><br>")

con.close() 