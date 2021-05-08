import config as cf
from sqlalchemy import create_engine
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date

engine = create_engine('mysql://sql6410935:GHh4XfMTfT@sql6.freesqldatabase.com:3306/sql6410935')
meta = MetaData()

corona = Table(
   'corona', meta, 
   Column('date', Date,), 
   Column('country', String(255)), 
   Column('confirmed', Integer()),
   Column('recovered', Integer()),
   Column('deaths', Integer()),
)

meta.create_all(engine)
print("These are columns in our table %s" %(corona.columns.keys()))