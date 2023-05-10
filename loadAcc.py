import os
import sqlite3

def allAcc():
        data_con = sqlite3.connect('userdb.db')
        spent = data_con.cursor()
        
        data = spent.execute("SELECT * FROM users").fetchall()

        return data