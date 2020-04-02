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

df = pandas.DataFrame()
#for i in range(len(records)):
    

#output_file("tile.html")

#tile_provider = get_provider(CARTODBPOSITRON)

# range bounds supplied in web mercator coordinates
#p = figure(x_range=(-2000000, 6000000), y_range=(-1000000, 7000000),
           #x_axis_type="mercator", y_axis_type="mercator")
#p.add_tile(tile_provider)

#show(p)
#save(p)