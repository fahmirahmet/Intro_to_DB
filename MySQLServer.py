import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="fhm1997???"  
)

cursor = connection.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
print("Database 'alx_book_store' created successfully!")


cursor.close()
connection.close()
