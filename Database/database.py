import os
import sqlite3


FOLDER_NAME = "Database"
DATABASE_NAME = os.path.join(FOLDER_NAME,"Phonebook.db")


def init_database():
    if not os.path.exists(FOLDER_NAME):
        os.mkdir(FOLDER_NAME)
    
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()

        cursor.execute(
            """
                CREATE TABLE IF NOT EXISTS Phonebook_data(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT NOT NULL,
                Phone_no INTEGER,
                Address TEXT,
                City TEXT,
                Pincode INTEGER)
            """
        )

def insert_contact(name, phone, address="", city="",pincode=""):
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """ INSERT INTO Phonebook_data (Name, Phone_no, Address, City, Pincode) VALUES(?,?,?,?,?)
            """,(name, phone, address, city, pincode),
        )
        conn.commit()