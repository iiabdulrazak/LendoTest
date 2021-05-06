import MySQLdb
import csv
import sys
import config

conn = MySQLdb.connect(host=host, user=user, password=password, database=database)

cursor = conn.cursor()
csv_data = csv.reader(open('../data/covidCases.csv'))
header = next(csv_data)

print('Importing the CSV Files')
for row in csv_data:
    print(row)
    cursor.execute(
        "INSERT INTO corona (date,country,confirmed,recovered,deaths) VALUES (%s, %s, %s, %s, %s)", row)

conn.commit()
cursor.close()
print('Done')

'''
import sqlalchemy
import pandas as pd


#creating engine to be able of connecting to the database,
#we gonna use 'sqlalchemy' to build the engine and 'mysql' as my database,
#the structure would be: ‘mysql://username:password@databasehost:port/databasename’

# Create the engine to connect to the MySQL database
engine = sqlalchemy.create_engine('mysql://sql6410213:GdeWcDcBxd@sql6.freesqldatabase.com:3306/sql6410213')
# Read data from CSV and load into a dataframe object
data = pd.read_csv('../data/covidCases.csv')
# Write data into the table in MySQL database
data.to_sql('corona-test',engine)
'''

#first method is the slowest because of the looping process,
#second method is the fasts because of the optimaization using pyPackage