import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='admin'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE dcrmdb")
print("All done")
