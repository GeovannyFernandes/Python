import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  port="3306",
  passwd=""
  
)

print(mydb)