import os
import sqlite3

def database():
    db_path = os.path.join(os.path.dirname(__file__), 'userdb.db')

    data_con = sqlite3.connect(db_path)
    users = data_con.cursor()

    users.execute("""CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER,
        username TEXT NOT NULL,
        employee_id TEXT NOT NULL,
        time_in TEXT NULL,
        time_out TEXT NULL,
        PRIMARY KEY(user_id AUTOINCREMENT))
        """)

    data_con.commit()
    
    data_con.close()
