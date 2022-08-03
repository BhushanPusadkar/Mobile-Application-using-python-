#!C:\Users\welcome\AppData\Local\Programs\Python\Python39\python
import cgi
import mysql.connector

print("content-type: text/html")
print()

print("<link rel='stylesheet' href='style.css' class=css />")
          
print("<style>body {font-family: Segoe UI, Tahoma, Geneva, Verdana, sans-serif;font-weight: bold;} .container { height: 900px;width: 400px;background-image: linear-gradient(#1e6b30, #308d46); top: 50%;left: 50%;position: absolute;transform: translate(-50%, -50%);position: absolute;border-bottom-left-radius: 180px;border-top-right-radius: 150px;} .main-content {height: 235px;background-color: #1b9236;border-bottom-left-radius: 90px;border-bottom-right-radius: 80px;border-top: #1e6b30;}.text {text-align: center;font-size: 300%;text-decoration: aliceblue;color: aliceblue;}.course {color: black;font-size: 25px;font-weight: bolder;}.centre-content {height: 180px;margin: -70px 30px 20px;color: aliceblue; text-align: center; font-size: 20px;border-radius: 25px; padding-top: 0.5px;  background-image: linear-gradient(#1e6b30, #308d46);}.centre-content-h1 { padding-top: 30px;padding-bottom: 30px;font-weight: normal;}</style>")
print("<div class='container'>")
print("<br><br><h2 style='background-color : plum; text-align:center; margin-left:390px; width:800px; padding:30px;'>Search Result</h2><hr>")





con=mysql.connector.connect(host='localhost',user='root',password='Bhushan@123',database='python')
curs=con.cursor()

request=cgi.FieldStorage()
s=request.getvalue("search")

curs.execute("select name,address,pincode,city from mobile where name='%s'" %s)
rec=curs.fetchone()



try:
    
    print("<fieldset>")
    print("<br><br> Customer Name      : %s" %rec[0])
    print("<br>Address     : %s" %rec[1])
    print("<br>Pin Code       : %s" %rec[2])
    print("<br>City   : %s" %rec[3])
    

    print("<form action='index.html'>")
    print("<input type='submit' value='No'>")
    print("</form>")
    print("<br></fieldset>")
    
except:
    print("<br><br><br><br><h1>mobile not found</h1><br><br><br><br><br>")

con.close() 
