import os
import mysql.connector
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

try:
    # Connect to MySQL Server using getenv
    mydb = mysql.connector.connect(
        host="localhost",
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

    if mydb.is_connected():
        mycursor = mydb.cursor()
        # Create the database if it doesn't exist
        mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as e:  # ✅ ALX expects this exact syntax
    print(f"Error while connecting to MySQL: {e}")

finally:
    if 'mydb' in locals() and mydb.is_connected():
        mycursor.close()
        mydb.close()
        print("MySQL connection is closed.")
