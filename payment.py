#!C:\Users\welcome\AppData\Local\Programs\Python\Python39\python 
import cgi 
import mysql.connector

print("content-type: text/html")
print()
request=cgi.FieldStorage()

mn=request.getvalue("name")
c=request.getvalue("gender")
p=request.getvalue("email")
s=request.getvalue("numaber")
r=request.getvalue("card_type")
fc=request.getvalue("card_number")
bc=request.getvalue("exp_date")
sim=request.getvalue("cvv")
n=request.getvalue("amount")


con=mysql.connector.connect(host='localhost',user='root',password='Bhushan@123',database='python')
curs=con.cursor()

try:

    curs.execute("insert into payment values('%s','%s','%s','%s','%s','%s','%s','%s','%s');" %(mn,c,p,s,r,fc,bc,sim,n))
    con.commit()
    print("<h3>User Registration Successful</h3>")
    print("<html>")
    print("<head>")
    print("<meta http-equiv='refresh' content='0;url=Adress.html'/>")
    print("</head>")
    print("</html>")
except :
    
    print("<h3><center>information not save..<center></h3>")    
    
    print("<br><br><a href='payment.html'>Home</a>")