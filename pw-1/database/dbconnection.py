import mysql.connector

try:
    db=mysql.connector.connect(
        host="localhost",
        user="root",
        password="Ganesh@16",
        database="pw1"
        )
    print("database connected..!!")
except mysql.connector.Error as e:
    print(f"There is some error connecting to the database {e}")