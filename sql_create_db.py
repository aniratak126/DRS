# sql_create_db.py
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
)

my_cursor = mydb.cursor()

my_cursor.execute("CREATE DATABASE USERS")
