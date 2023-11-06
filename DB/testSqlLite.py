import sqlite3
from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB sucD:\Sqllitecessful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

create_connection("D:\Sqllite\sql_sample.dat")