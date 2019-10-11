# Part 1: Making and populating a database.

import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')

conn.execute('''CREATE TABLE demo (s, x, y);''')

c = conn.cursor()

c.execute("INSERT INTO demo VALUES ('g','3','9');")
c.execute("INSERT INTO demo VALUES ('v','5','7');")
c.execute("INSERT INTO demo VALUES ('f','8','7');")

for row in c.execute('SELECT * FROM demo;'):
    print(row)

x = c.execute('SELECT COUNT(s) FROM demo;') # 3 rows in total in memory address.
print(c.fetchmany())
y = c.execute('SELECT COUNT(DISTINCT y) FROM demo;') # 2 distict values. 
print(c.fetchone())

conn.commit()
conn.close()