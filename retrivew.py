#!C:\Users\welcome\AppData\Local\Programs\Python\Python39\python
import cgi
import mysql.connector

print("content-type: text/html")
print()

print("<link rel='stylesheet' href='bootstrap.min.css'>")
print("<style>body{ background-repeat:no-repeat; background-size:500px 650px;}fieldset { border-radius:20px; margin-left:360px; border:3px solid plum; background-color:purple; width:80%; color:white; font-weight:bold; padding:40px; font-size:20px; }</style>")
print("<div class='container'>")
print("<br><br><h2 style='background-color : plum; text-align:center; margin-left:390px; width:800px; padding:30px;'>Search Result</h2><hr>")
con=mysql.connector.connect(host='localhost',user='root',password='Bhushan@123',database='python')
curs=con.cursor()

request=cgi.FieldStorage()
s=request.getvalue("search")

curs.execute("select name,color,processor,storage,ram,fcamera,bcamera,sim,network,battery,display,price from mobile where name='%s'" %s)
rec=curs.fetchone()


try:
    
    print("<fieldset>")
    print("The information of Mobile Name :- %s" %rec[0])
    print(" is ")
    print("<br><br>Name      : %s" %rec[0])
    print("<br>Color      : %s" %rec[1])
    print("<br>Processor        : %s" %rec[2])
    print("<br>Storage   : %s" %rec[3])
    print("<br>Ram       : %s" %rec[4])
    print("<br>fcamera        : %s" %rec[5])
    print("<br>bcamera        : %s" %rec[6])
    print("<br>sim        : %s" %rec[7])
    print("<br>network        : %s" %rec[8])
    print("<br>battery        : %s" %rec[9])
    print("<br>display       : %s" %rec[10])
    print("<br>price       : %s" %rec[11])



    
    print("<hr style='background-color:white;''>")
    print("Do you want to delete this mobile?")
    print("<form action='delete.html'>")
    print("<br><input type='submit' value='Yes'>")

    print("</form>")

   

    print("<form action='retrivew.html'>")
    print("<input type='submit' value='No'>")
    print("</form>")
    print("<br></fieldset>")
    
except:
    print("<br><br><br><br><h1>mobile not found</h1><br><br><br><br><br>")

con.close() 