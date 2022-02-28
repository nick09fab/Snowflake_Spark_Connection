!pip install snowflake-connector-python

import snowflake.connector

conn = snowflake.connector.connect(
    user = 'suser',
    password = 'P@$sW0rd',
    account = 'abc123.us-east-2',
    warehouse = 'demo_wh',
    database = 'demo',
    schema = 'PUBLIC'
)
#create cursor
curs = conn.cursor()

#execute SQL statement
curs.execute('select * from table_name_snowflake')

#fetch result
for row in curs:
    print(row)

# Store it as a dataframe,table or write it as a csv file
 
