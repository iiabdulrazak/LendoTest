import MySQLdb
import csv
import sys
import config as cf
from sqlalchemy import create_engine
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date

#needed configuration and connection
meta = MetaData()
conn = MySQLdb.connect(host='172.105.154.40', user='AdminLiquidX', password='Zaak1234@', database='prodDB')
cursor = conn.cursor()
engine = create_engine('mysql://AdminLiquidX:Zaak1234@@172.105.154.40:22/prodDB')

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