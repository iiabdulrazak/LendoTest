import MySQLdb
import csv
import sys
import config as cf

conn = MySQLdb.connect(host=cf.host, user=cf.user, password=cf.password, database=cf.database)

cursor = conn.cursor()
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