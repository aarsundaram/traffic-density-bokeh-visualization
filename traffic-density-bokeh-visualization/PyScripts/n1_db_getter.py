import bokeh
import pandas
import time
import mysql.connector as mysql

db = mysql.connect(
    host="localhost",
    user="root",
    passwd="Ingismyfocus@21",
    database='epa1351group17'
)

cursor = db.cursor()
#output_file('n1_viz.html')

query = "SELECT * FROM createtrucks"
cursor.execute(query)
records= cursor.fetchall()

df1 = pandas.DataFrame()

for i in range(len(records)):
    df = pandas.DataFrame()
    ids = []
    hour = []
    src = []
    number = []

    ids.append(records[i][0])
    hour.append(records[i][1])
    src.append(records[i][2])
    number.append(records[i][3])

    df = pandas.DataFrame({'id': ids, 'hour': hour, 'source': src,'number': number})
    df1 = pandas.concat([df1, df], ignore_index=True)


df1.to_csv('n1_trucks.csv')



