# import sqlite3
# conn=sqlite3.connect('data.db')
# cur=conn.cursor()
#
# cur.execute('''
# CREATE TABLE IF NOT EXISTS(
# id INTEGER PRIMARY KEY,
# username TEXT NOT NULL,
# email TEXT NOT NULL,
# age INTEGER
# )
# ''')
#
# cur.execute('INSERT INTO Users(id, username, email, age)')
# conn.commit()
#
# conn.close()