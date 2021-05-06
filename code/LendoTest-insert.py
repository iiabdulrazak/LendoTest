import sqlalchemy as db
import pandas as pd

#creating engine to be able of connecting to the database,
#we gonna use 'sqlalchemy' to build the engine and 'mysql' as my database,
#the structure would be: ‘mysql://username:password@databasehost:port/databasename’
print('Inserting in Process ...!')
# Create the engine to connect to the MySQL database
engine = db.create_engine('mysql://sql6410692:DHD7HJS6Yj@sql6.freesqldatabase.com:3306/sql6410692')
# Read data from CSV and load into a dataframe object
data = pd.read_csv('../data/covidCases.csv')
# Write data into the table in MySQL database
data.to_sql('corona',engine)
print('Inserting Compeleted!')

'''
first method(LendoTest-insert-beta.txt) is the slowest because of the,
looping process, second method is the fasts because of the optimaization
using sqlalchemy package
'''