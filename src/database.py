import sqlite3, threading, os

path = "../config/database.db"

db_conn = None
cursor = None
database_lock = None

# create database of Homebridge accessories and its current state
def create_database() -> None:
    global path, db_conn, cursor, database_lock

    # check if there is not any database file from previous script run
    if os.path.isfile(path):
        os.remove(path)

    # connect to accessories database
    db_conn = sqlite3.connect(path, check_same_thread = False)

    # create cursor
    cursor = db_conn.cursor()

    # create lock object
    database_lock = threading.Lock()

    # create Accessories table
    database_lock.acquire(True)
    cursor.execute("""
        create table if not exists Accessories (
            uniqueId text primary key,
            serviceName text,
            currentState text,
            lastModified text
            ); """)
    database_lock.release()

# commit changes, close connection with database and delete file
def remove_database() -> None:
    global database_lock, db_conn, path
    
    database_lock.acquire(True)
    db_conn.commit()
    db_conn.close()
    database_lock.release()

    os.remove(path)



#database_lock.acquire(True)
#cursor.execute("UPDATE Reminder SET notified = ? WHERE rowid = ?;", (notified, id))
#db_conn.commit()
#database_lock.release()