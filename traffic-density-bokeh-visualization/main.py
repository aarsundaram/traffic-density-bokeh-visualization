from bokeh.plotting import figure, output_file, save, show
from bokeh.tile_providers import CARTODBPOSITRON, get_provider
import pandas
# Connecting to the database

## importing 'mysql.connector' as mysql for convenient
import mysql.connector as mysql

## connecting to the database using 'connect()' method
## it takes 3 required parameters 'host', 'user', 'passwd'
db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "einstein",
    database='datacamp'
)
cursor=db.cursor()
## defining the Query
query = "SELECT * FROM users"
## getting records from the table
cursor.execute(query)
records=cursor.fetchall()
cols= ["ind","name","username"]
df1=pandas.DataFrame()

for i in range(len(records)):
    df=pandas.DataFrame()    
    names=[]
    usernames=[]
    ids=[]

    ids.append(records[i][0])
    names.append(records[i][1])
    usernames.append(records[i][2])


    df = pandas.DataFrame({'id':ids,'names':names,'usernames':usernames})
    df1=pandas.concat([df1,df],ignore_index=True)

numbers=[25,98,55,67,130]
df1['numbers']=numbers
print(df1)

names1=df1['names']
numbers1=df1['numbers']

output_file("tile.html")

p=figure(
    title='simple example',
    x_axis_label='names',
    y_axis_label='costs',
    
)
p.line(names1,numbers1,legend='test',line_width=2)

show(p)
#save(p)