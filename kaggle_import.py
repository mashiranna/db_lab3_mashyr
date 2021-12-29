import csv
import psycopg2

con = psycopg2.connect(user='mashyr_anna', password='1234', dbname='mashyr_anna_DB', host='localhost', port='5432')
print(type(con))

INPUT_CSV = 'windows_store.csv'

query_0 = '''
CREATE TABLE app_new_new
( 
    Name     character varying(1000) UNIQUE NOT NULL,
    Publisher    character varying(1000) NOT NULL,
    Price        character varying(100) NOT NULL,
    PRIMARY KEY (Name)
)
'''

query_1 = '''
DELETE FROM app_new_new
'''

query_2 = '''
INSERT INTO app_new_new(Name, Publisher, Price) VALUES (%s, %s, %s)
'''


with con:
    cur = con.cursor()
    cur.execute('drop table if exists app_new_new')
    cur.execute(query_0)
    cur.execute(query_1)

    with open(INPUT_CSV, 'r', encoding="utf8") as inf:
        reader = csv.DictReader(inf)

        for idx, row in enumerate(reader):
            values = (row['Name'], row['Publisher'], row['Price'])
            cur.execute(query_2, values)

    con.commit()

