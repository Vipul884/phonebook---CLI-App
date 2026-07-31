import os
import sqlite3


FOLDER_NAME = "Database"
DATABASE_NAME = os.path.join(FOLDER_NAME,"Phonebook.db")


def init_database():
    if not os.path.exists(FOLDER_NAME):
        os.mkdir(FOLDER_NAME)
    
    conn = sqlite3.connect(DATABASE_NAME)
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

    conn.commit()
    conn.close()
    print("Database aur Tables setup ho gaye hain!")

init_database()