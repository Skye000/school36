import sqlite3
conn=sqlite3.connect('data.db')
cur=conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS
''')

conn.close()