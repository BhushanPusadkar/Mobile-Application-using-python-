#!C:\Users\welcome\AppData\Local\Programs\Python\Python39\python
import cgi
import mysql.connector

print("content-type: text/html")
print()

print("<link rel='stylesheet' href='bootstrap.min.css'>")
print("<style>body{ background-image:url(image/girl.gif); background-size:800px 850px;}fieldset { border-radius:20px; margin-left:360px; border:3px solid black; background-color:skyblue; width:40%; color:black; font-weight:bold; padding:40px; font-size:20px; }</style>")
print("<div class='container'>")
print("<br><br><h2 style='background-color : powderblue; text-align:center; margin-left:390px; width:400px; padding:30px;'>Search Result</h2><hr>")
con=mysql.connector.connect(host='localhost',user='root',password='Bhushan@123',database='python')
curs=con.cursor()

request=cgi.FieldStorage()
m=request.getvalue("search")

curs.execute("select name,color,processor,storage,ram,fcamera,bcamera,sim,network,battery,display,price from mobile where name='%s'" %m)
rec=curs.fetchone()


try:
    print("<fieldset>")
    
    print("<br><br>name : %s" %rec[0])
    print("<br><br>Color     : %s" %rec[1])
    print("<br><br>processor        : %s" %rec[2])
    print("<br><br>Storage   : %d" %rec[3])
    print("<br><br>Ram      : %d" %rec[4])
    print("<br><br>Front Camera      : %d" %rec[5])
    print("<br><br>Back Camera        : %d" %rec[6])
    print("<br><br>Sim   : %s" %rec[7])
    print("<br><br>Network    : %d" %rec[8])
    print("<br><br>battery      : %d" %rec[9])
    print("<br><br>display  : %s" %rec[10])
    print("<br><br>price    : %d" %rec[11])
    
    #print("<br><br>image : %s" %PIL.show(r,"%s"%rec[12]))
    
    print()
    
    print("<br></fieldset>")
except:
    print("<br><br><br><br>mobile not found<br><br><br><br><br>")

con.close() 