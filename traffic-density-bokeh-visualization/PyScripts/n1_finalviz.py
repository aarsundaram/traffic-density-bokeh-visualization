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

### reading in createtrucks & creating df
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

    df = pandas.DataFrame({'id': ids, 'Time': hour, 'Segment': src,'Trucks': number})
    df1 = pandas.concat([df1, df], ignore_index=True)

### reading in destroyedvehicles & creating df
query = "SELECT * FROM destroyedvehicles"
cursor.execute(query)
records= cursor.fetchall()

df2 = pandas.DataFrame()

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

    df = pandas.DataFrame({'id': ids, 'Time': hour, 'Segment': src,'DestroyVehicles': number})
    df2 = pandas.concat([df2, df], ignore_index=True)

### reading in createcars & creating df
query = "SELECT * FROM createcars"
cursor.execute(query)
records= cursor.fetchall()

df3 = pandas.DataFrame()

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

    df = pandas.DataFrame({'id': ids, 'Time': hour, 'Segment': src,'Cars': number})
    df3 = pandas.concat([df3, df], ignore_index=True)
