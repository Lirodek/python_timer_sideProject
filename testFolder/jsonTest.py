import sqlite3

con = sqlite3.connect('person.db')
cur = con.cursor()

con.commit()

for row in cur.execute('SELECT * FROM person ORDER BY name'):
    print(row[1])
    
cur.close() 