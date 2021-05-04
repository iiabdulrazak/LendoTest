import MySQLdb
import csv
import sys
import configuration

host="sql6.freesqldatabase.com"
user="sql6410213"
password="GdeWcDcBxd"
database="sql6410213"

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