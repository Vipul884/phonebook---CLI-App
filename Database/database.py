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

def view():
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute(""" 
        SELECT * FROM Phonebook_data;
        
        """)
        data = cursor.fetchall()
        print(f"{'ID':<5} {'Name':<20} {'Phone':<15} {'Address':<25} {'City':<15} {'Pincode':<10}")
        print("-" * 95)
        
        for id, name, phone, address, city, pincode in data:
            print(f"{id:<5} {name:<20} {phone:<15} {address:<25} {city:<15} {pincode:<10}")
            
def search_contact():
    choice = input("Search by Name / Phone / Address / City / Pincode ?:  ").lower()

    value = input("Enter the Value: ")

    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        
        if choice == "name":
            query = "SELECT * FROM Phonebook_data WHERE LOWER(Name) LIKE LOWER(?);"
            search_value = f"%{value}%"
        elif choice == "phone":
            query = "SELECT * FROM Phonebook_data WHERE Phone_no =?;"
            search_value = value
        elif choice == "address":
            query = "SELECT * FROM Phonebook_data WHERE Address =?;"
            search_value = value
        elif choice == "city":
            query = "SELECT * FROM Phonebook_data WHERE LOWER(City) =?;"
            search_value = value
        elif choice == "pincode":
            query = "SELECT * FROM Phonebook_data WHERE Pincode =?;"
            search_value = value
        else:
            print("Invalid Choice")
            return

        cursor.execute(query,(search_value,))
        data = cursor.fetchall()

        if data:
            print(f"{'ID':<5} {'Name':<20} {'Phone':<15} {'Address':<25} {'City':<15} {'Pincode':<10}")
            print("-" * 95)
            for id, name, phone, address, city, pincode in data:
                print(f"{id:<5} {name:<20} {phone:<15} {address:<25} {city:<15} {pincode:<10}")
        else:
            print(f"No Record Found with this {choice}: {value} !")

