import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv 

try:
    # Connect to MySQL Server
    mydb = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),       
        password=os.getenv("DB_PASSWORD")      
    )

    if mydb.is_connected():
        mycursor = mydb.cursor()
        # Create database if it doesn't exist
        mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    # Close connection
    if 'mydb' in locals() and mydb.is_connected():
        mycursor.close()
        mydb.close()
        print("MySQL connection is closed.")
