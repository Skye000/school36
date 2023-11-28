import sqlite3
class DB_maneger():
    def __init__(self, path):
        self.conn=sqlite3.connect(path)
        self.conn.commit()
        self.cur=self.conn.cursor()


    def qery(self, arg, values=None):
        if values==None:
            self.cur.execute(arg)
        else:
            self.cur.execute(arg, values)
        self.conn.commit()


    def create_tables(self):
        self.qery('''CREATE TABLE IF NOT EXISTS Users(Name TEXT NOT NULL, LastName TEXT NOT NULL, email TEXT NOT NULL )''')


    def fetchall(self, arg, values=None):
        if values==None:
            self.cur.execute(arg)
        else:
            self.cur.execute(arg, values)
        return self.cur.fetchall()
    def fetchone(self, arg, values=None):
        if values==None:
            self.cur.execute(arg)
        else:
            self.cur.execute(arg, values)
        return self.cur.fetchone()

    def __del__(self):
        self.conn.close()