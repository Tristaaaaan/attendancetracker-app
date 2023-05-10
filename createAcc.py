import os
import bcrypt
import sqlite3

def storeAcc(username, employee_id):

    db_path = os.path.join(os.path.dirname(__file__), 'userdb.db')

    data_con = sqlite3.connect(db_path)
    users = data_con.cursor()

    users.execute("INSERT into users (username, employee_id) values(?, ?)", (
                    username,
                    employee_id
                    ))

    data_con.commit()

    data_con.close()