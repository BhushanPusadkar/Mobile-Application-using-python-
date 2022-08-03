#!C:\Users\welcome\AppData\Local\Programs\Python\Python39\python
import mysql.connector

print("content-type: text/html")
print()

print("<link rel='stylesheet' href='bootstrap.min.css'>")
print("<div class='container'>")
print("<style>table th {font-weight : bolder; font-size : 23px;} h2 {color :  black;} body { background-image: url(image/back.jpg); background-size : 1600px 900px} table {box-shadow: 100px 100px 100px powderblue;} a {animation: bounching 0.5s ease 0s infinite alternate both; border-radius: 50%; display: inline-block;color: white;cursor: pointer; font-size: 0.95rem; margin-top: 20px; font-weight: 1000; vertical-align: top; text-align: right; position: relative; padding: 1em 2.5em 1.2em; background: green;} @keyframes bounching {0% {bottom: 0;box-shadow: 0 0 5px black;}100% {bottom: 0px;box-shadow: 0 50px 50px black;}}</style>")
con=mysql.connector.connect(host='localhost',user='root',password='Bhushan@123',database='python')
curs=con.cursor()

curs.execute("select * from register")
all=curs.fetchall()

print("<br><br><h2>User Information</h2><hr>")
print("<table class='table table-bordered table-hover'>")
print("<tr style='background-color:pink'>")

print("<th style='background-color:skyblue'>User_id")
print("<th style='background-color:skyblue'>password")
print("<th style='background-color:skyblue'>confirm password")
print("<th style='background-color:skyblue'>UserName")
print("<th style='background-color:skyblue'>address")
print("<th style='background-color:skyblue'>mobile")


for one in all:
    print("<tr>")
    print("<td>%s" %one[0])
    print("<td>%s" %one[1])
    print("<td>%s" %one[2])
    print("<td>%s" %one[3])
    print("<td>%s" %one[4])
    print("<td>%s" %one[5])
    
    
    print("</tr>")

print("</table>")
print("</div>")

print("<hr><center><a href='index.html'> Back </a><center>")

con.close()    