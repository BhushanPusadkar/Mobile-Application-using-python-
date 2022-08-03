#!C:\Users\welcome\AppData\Local\Programs\Python\Python39\python
import cgi
import mysql.connector

print("content-type: text/html")
print()

print("<link rel='stylesheet' href='bootstrap.min.css'>")
# print("<style>body{ background-image:url(image/girl.gif); background-size:800px 850px;}fieldset { border-radius:20px; margin-left:360px; border:3px solid plum; background-color:purple; width:40%; color:white; font-weight:bold; padding:40px; font-size:20px; }</style>")
print("<div class='container'>")
# print("<br><br><h2 style='background-color : plum; text-align:center; margin-left:390px; width:400px; padding:30px;'>Search Result</h2><hr>")



request=cgi.FieldStorage()

n=request.getvalue("name")
p=request.getvalue("price")

con=mysql.connector.connect(host='localhost',user='root',password='Bhushan@123',database='python')
curs=con.cursor()

try:
    curs.execute(" update mobile set price='%s' where name='%s';"%(p,n))
    con.commit()
    print("<h3><center>Update  Successfull</center></h3>")
    print("<hr><center><a href='index.html'> Back </a><center>")

except:
    print("<h3><center>update failed..<center></h3>")  
