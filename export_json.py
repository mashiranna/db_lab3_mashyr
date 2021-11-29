import json
import psycopg2

con = psycopg2.connect(user='mashyr_anna', password='1234', dbname='mashyr_anna_DB', host='localhost', port='5432')
print(type(con))

TABLES = [
    'age_rating',
    'app',
    'app_publisher',
    'category']

data = {}

with con:
    cur = con.cursor()

    for table_name in TABLES:
        cur.execute('select * from ' + table_name)
        fields = [x[0] for x in cur.description]
        rows = []

        for row in cur:
            rows.append(dict(zip(fields, row)))

        data[table_name] = rows

with open('mashyr_all.json', 'w') as outfile:
    json.dump(data, outfile, default=str)
