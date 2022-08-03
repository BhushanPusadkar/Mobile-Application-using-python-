#!C:\Users\welcome\AppData\Local\Programs\Python\Python39\python
import cgi 
import mysql.connector

print("content-type: text/html")
print()
request=cgi.FieldStorage()

mn=request.getvalue("name")
c=request.getvalue("color")
p=request.getvalue("processor")
s=request.getvalue("storage")
r=request.getvalue("ram")
fc=request.getvalue("fcamera")
bc=request.getvalue("bcamera")
sim=request.getvalue("sim")
n=request.getvalue("network")
bt=request.getvalue("battery")
d=request.getvalue("display")
pr=request.getvalue("price")

con=mysql.connector.connect(host='localhost',user='root',password='Bhushan@123',database='python')
curs=con.cursor()

try:

    curs.execute("insert into mobile values('%s','%s','%s','%s', '%s', '%s', '%s','%s','%s', '%s','%s','%s')" %(mn,c,p,s,r,fc,bc,sim,n,bt,d,pr))
    con.commit()
    print("<h3>User Registration Successful</h3>")
    
except :
    
    print("<h3><center>Mobile not Added..<center></h3>")    
    
    print("<br><br><a href='index.html'>Home</a>")