import pandas as pd
import sqlalchemy
    
# Create the engine to connect to the MySQL database,
engine = sqlalchemy.create_engine('mysql://sql6410213:GdeWcDcBxd@sql6.freesqldatabase.com:3306/sql6410213')
# Read data from SQL table
# we use read_sql_table to read the data using pandas commands
sql_data = pd.read_sql_table('corona',engine)

#now lets see the table
print(f'Database Data:\n{sql_data.head()}\n\n')
print(f'{sql_data.info()}')

#lets start manipulating with the database,
#we use read_sql to read from database using sql commands
sql_data_all = pd.read_sql(
	"SELECT * FROM corona;",
	engine,
	parse_dates = ['date']
	)

sql_data_col = pd.read_sql(
	"SELECT confirmed FROM corona;",
	engine,
	parse_dates = ['date']
	)

sql_data_count = pd.read_sql(
	"SELECT COUNT(confirmed) FROM corona;",
	engine,
	parse_dates = ['date']
	)

print(f'{sql_data_all}')
print(f'\n\n{sql_data_col}')
print(f'\n\n{sql_data_count}')