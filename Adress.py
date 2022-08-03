#!C:\Users\welcome\AppData\Local\Programs\Python\Python39\python
import cgi
import mysql.connector

print("content-type: text/html")
print()

print("<link rel='stylesheet' href='bootstrap.min.css'>")
print("<style>body{ background-image:url(image/girl.gif); background-size:800px 850px;}fieldset { border-radius:20px; margin-left:360px; border:3px solid black; background-color:skyblue; width:40%; color:black; font-weight:bold; padding:40px; font-size:20px; }</style>")
print("<div class='container'>")
print("<br><br><h2 style='background-color : powderblue; text-align:center; margin-left:390px; width:400px; padding:30px;'>Address is</h2><hr>")
con=mysql.connector.connect(host='localhost',user='root',password='Bhushan@123',database='python')
curs=con.cursor()

request=cgi.FieldStorage()
m=request.getvalue("search")

curs.execute("select * from users where usernm='%s'" %m)
rec=curs.fetchone()


try:
    print("<fieldset>")
    
    print("<br><br>Address : %s" %rec[4])
    
    print()
    
    
    print("<br><br><br>")
    print('<style>input[type="submit"] {background-color: green;border: 1px solid black;margin-left: 200px;color: azure;width: 50%;font-weight: 700;cursor: pointer;padding: 8px; }</style>')
    print("do you want to change the Address? ...")
    print('<form action="change.py">  <center><tr><td><h4>Enter your user name</h4></td><td><input type="text" name="search" class="form-control" required></td><td><br></td><td><input type="text" name="adress" class="form-control" required></td><td> <input type="submit" value="Change Address"></td></tr></form>')
    print('<a href="Index.html">---->back</a>')
    print("<br></fieldset>")
except:
    print("<br><br><br><br>Address not found<br><br><br><br><br>")

con.close() 