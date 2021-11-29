import psycopg2
import matplotlib.pyplot as plt


query_1 = '''
create view CategoryQuantity as 
    select category, count(category) from app group by category
'''
query_2 = '''
create view AgeRatingQuantity as 
    select age_rating, count(age_rating) from app group by age_rating
'''

query_3 = '''
create view SizeAndDateOfRelease as 
select initial_date_of_release, app_size, app.app_name from app_publisher, app
where app_publisher.app_name = app.app_name
order by initial_date_of_release
'''

con = psycopg2.connect(user='mashyr_anna', password='1234', dbname='mashyr_anna_DB', host='localhost', port='5432')
print(type(con))

result_1 = []
result_2 = []
result_3 = []

with con:

    print("Database opened successfully")

    cur = con.cursor()

    cur.execute('drop view if exists CategoryQuantity')
    print('\n1.  ')
    cur.execute(query_1)

    cur.execute('select * from CategoryQuantity')
    for row in cur:
        print(row)
        result_1.append(row)

    cur.execute('drop view if exists AgeRatingQuantity')
    print('\n2.  ')
    cur.execute(query_2)
    cur.execute('select * from AgeRatingQuantity')
    for row in cur:
        print(row)
        result_2.append(row)

    cur.execute('drop view if exists SizeAndDateOfRelease')
    print('\n3.  ')
    cur.execute(query_3)
    cur.execute('select * from SizeAndDateOfRelease')
    for row in cur:
        print(row)
        result_3.append(row)


data_1 = {}
for i in range(len(result_1)):
    data_1[result_1[i][0]] = result_1[i][1]

plt.bar(data_1.keys(), data_1.values(), width=0.5)
plt.xlabel('Category')
plt.ylabel('Quantity')
# plt.show()
plt.savefig('1st.png')

data_2 = {}
for i in range(len(result_2)):
    data_2[result_2[i][0]] = result_2[i][1]

fig, ax = plt.subplots()
ax.pie(data_2.values(), labels=data_2.keys(), autopct='%1.1f%%', shadow=True, rotatelabels=True)
# plt.show()
plt.savefig('2st.png')
plt.clf()


def to_integer(dt_time):
    return 10000*dt_time.year + 100*dt_time.month + dt_time.day


x = []
y = []
data_3 = {}
for i in range(len(result_3)):
    data_3[to_integer(result_3[i][0])] = result_3[i][1]
    x.append(to_integer(result_3[i][0]))
    y.append(result_3[i][1])

plt.scatter(x, y)
plt.xlabel('Date of release')
plt.ylabel('Size')
# plt.show()
plt.savefig('3st.png')