
import pandas
import time
import mysql.connector as mysql

db = mysql.connect(
    host="localhost",
    user="root",
    passwd="Ingismyfocus@21",
    database='world'
)

cursor = db.cursor()

while true:
    try:
        query = "SELECT * FROM city"
        cursor.execute(query)
        records = cursor.fetchall()
        print(records)

    except:
        print("Error")
        db.rollback()
    time.sleep(5)

