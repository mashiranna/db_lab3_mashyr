import csv
import psycopg2

con = psycopg2.connect(user='mashyr_anna', password='1234', dbname='mashyr_anna_DB', host='localhost', port='5432')
print(type(con))

OUTPUT_FILE_T = 'mashyr_{}.csv'

TABLES = [
    'age_rating',
    'app',
    'app_publisher',
    'category']

with con:
    cur = con.cursor()

    for table_name in TABLES:
        cur.execute('select * from ' + table_name)
        fields = [x[0] for x in cur.description]

        with open(OUTPUT_FILE_T.format(table_name), 'w') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(fields)
            for row in cur:
                writer.writerow([str(x).lstrip() for x in row])
