import os
import bcrypt
import sqlite3

def locateUsername(employe_id):

    db_path = os.path.join(os.path.dirname(__file__), 'userdb.db')

    data_con = sqlite3.connect(db_path)

    users = data_con.cursor()

    users.execute("SELECT employee_id FROM users WHERE employee_id = ?", (employe_id,))

    usernamesdb = (res[0] for res in users.fetchall())
    
    if employe_id in usernamesdb:
        data_con.close()
        return True
    return False



def locateAcc(username, passw):

    db_path = os.path.join(os.path.dirname(__file__), 'userdb.db')

    data_con = sqlite3.connect(db_path)

    users = data_con.cursor()
    users.execute("SELECT salt, passw_hashed FROM users WHERE username = ?", (username,))

    # Storing the hashed password [1] and salt [0]
    data = users.fetchone()

    # Generating a hash of the entered password using the stored salt
    user_password = bcrypt.hashpw(passw.encode('utf-8'), data[0])

    # Matching the hashed entered password to the stored hashed password
    if user_password == data[1]:
        data_con.commit()
        data_con.close()
        return True
    return False