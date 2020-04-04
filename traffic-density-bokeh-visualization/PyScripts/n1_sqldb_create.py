import bokeh
from bokeh.plotting import figure, output_file, save, show
from bokeh.tile_providers import CARTODBPOSITRON, get_provider
import pandas
from bokeh.models import ColumnDataSource, Range1d
from bokeh.layouts import layout
from bokeh.palettes import Spectral3
from bokeh.tile_providers import CARTODBPOSITRON
from pyproj import Proj, transform


output_file('mapping_N1.html')


# Connecting to the database
import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "-",
    database= "epa1315group17"
)

## creating an instance of 'cursor' class which is used to execute the 'SQL' statements in 'Python'
cursor = db.cursor()

#creating database "epa1315group17" according to schema in Simio 
query= 'CREATE TABLE createbuses (id INT(11) NOT NULL AUTO_INCREMENT,Time DOUBLE DEFAULT NULL,Segment VARCHAR(100) DEFAULT NULL,Buses INT(11) DEFAULT NULL,PRIMARY KEY (id))'
cursor.execute(query)
query="SELECT * from createtrucks"
cursor.execute(query)
## getting records from the table
records=cursor.fetchall()

for record in records:
    print(record)
    
#query= "CREATE TABLE createcars (id INT(11) NOT NULL AUTO_INCREMENT,Time DOUBLE DEFAULT NULL,Segment VARCHAR(100) DEFAULT NULL, Cars INT(11) DEFAULT NULL, PRIMARY KEY (id))" 
#cursor.execute(query)

#query= "CREATE TABLE createtrucks (id INT(11) NOT NULL AUTO_INCREMENT,Time DOUBLE DEFAULT NULL,Segment VARCHAR(100) DEFAULT NULL, Trucks INT(11) DEFAULT NULL, PRIMARY KEY (id))" 
#cursor.execute(query)

#query= "CREATE TABLE destroyedvehicles (id INT(11) NOT NULL AUTO_INCREMENT,Time DOUBLE DEFAULT NULL,Segment VARCHAR(100) DEFAULT NULL, DestroyVehicles INT(11) DEFAULT NULL, PRIMARY KEY (id))" 
#cursor.execute(query)



