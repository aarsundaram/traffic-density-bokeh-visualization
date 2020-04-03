import bokeh
from bokeh.plotting import figure, output_file, save, show
from bokeh.tile_providers import CARTODBPOSITRON, get_provider
import pandas
# Connecting to the database

## importing 'mysql.connector' as mysql for convenient
import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "einstein",
    database= "epa1315group17"
)

## creating an instance of 'cursor' class which is used to execute the 'SQL' statements in 'Python'
cursor = db.cursor()


# creating database "epa1315group17" according to schema in Simio
#uncomment for creating in your own system 

#query= 'CREATE TABLE createbuses (id INT(11) NOT NULL AUTO_INCREMENT,Time DOUBLE DEFAULT NULL,Segment VARCHAR(100) DEFAULT NULL,Buses INT(11) DEFAULT NULL,PRIMARY KEY (id))'
#cursor.execute(query)

#query= "CREATE TABLE createcars (id INT(11) NOT NULL AUTO_INCREMENT,Time DOUBLE DEFAULT NULL,Segment VARCHAR(100) DEFAULT NULL, Cars INT(11) DEFAULT NULL, PRIMARY KEY (id))" 
#cursor.execute(query)

#query= "CREATE TABLE createtrucks (id INT(11) NOT NULL AUTO_INCREMENT,Time DOUBLE DEFAULT NULL,Segment VARCHAR(100) DEFAULT NULL, Trucks INT(11) DEFAULT NULL, PRIMARY KEY (id))" 
#cursor.execute(query)

#query= "CREATE TABLE destroyedvehicles (id INT(11) NOT NULL AUTO_INCREMENT,Time DOUBLE DEFAULT NULL,Segment VARCHAR(100) DEFAULT NULL, DestroyVehicles INT(11) DEFAULT NULL, PRIMARY KEY (id))" 
#cursor.execute(query)


cursor.execute(query)
