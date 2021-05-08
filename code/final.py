import MySQLdb
import csv
import sys
import config as cf
from sqlalchemy import create_engine
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date

#needed configuration and connection
meta = MetaData()
cursor = conn.cursor()
conn = MySQLdb.connect(host=cf.host, user=cf.user, password=cf.password, database=cf.database)
engine = create_engine('mysql://sql6410935:GHh4XfMTfT@sql6.freesqldatabase.com:3306/sql6410935')

#creating table
corona = Table(
   'corona', meta, 
   Column('date', Date,), 
   Column('country', String(255)), 
   Column('confirmed', Integer()),
   Column('recovered', Integer()),
   Column('deaths', Integer()),
)

meta.create_all(engine)
print("Table Created! %s" %(corona.columns.keys()))

#inserting to the table
csv_data = csv.reader(open('../data/covidCases.csv'))
header = next(csv_data)
print('Inserting in Process ...!')
for row in csv_data:
    print(row)
    cursor.execute(
        "INSERT INTO corona (date,country,confirmed,recovered,deaths) VALUES (%s, %s, %s, %s, %s)", row)

conn.commit()
cursor.close()
print('Process Done!')
print("Table Created! %s" %(corona.columns()))