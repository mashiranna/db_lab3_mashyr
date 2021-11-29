import csv
import psycopg2

con = psycopg2.connect(user='mashyr_anna', password='1234', dbname='mashyr_anna_DB', host='localhost', port='5432')
print(type(con))

INPUT_CSV_FILE = 'app.csv'

query_1 = '''
CREATE TABLE app_new
( 
    app_name     character varying(60),
    publisher    character varying(50),
    price        character varying(50),
    description  character varying(1600),
    app_size     character varying(50),
    category     character varying(30),
    age_rating   character varying(30),
    CONSTRAINT app_name PRIMARY KEY (app_name)
)
'''

query_2 = '''
DELETE FROM app_new
'''

query_3 = '''
INSERT INTO app_new (app_name, publisher, price, description, app_size, category, age_rating ) VALUES (%s, %s, %s, %s, %s, %s ,%s)
'''


with con:

    cur = con.cursor()
    cur.execute('drop  table if exists app_new')
    cur.execute(query_1)
    cur.execute(query_2)

    with open(INPUT_CSV_FILE, 'r') as file:
        reader = csv.DictReader(file)

        for idx, row in enumerate(reader):
            values = (idx, row['Name'], row['Publisher'])
            cur.execute(query_2, values)

    con.commit()
