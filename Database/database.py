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
            search_value = value.lower()
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

def delete_all():
    try:
        with sqlite3.connect(DATABASE_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("""
            DELETE FROM Phonebook_data; 
            """)
            conn.commit()
    
    except Exception as e:
        print(f"Error in Database: {e}")


def edit_contact():

    try:
        value = input("Enter the Name of contact you want to edit ?:  ").lower()

        with sqlite3.connect(DATABASE_NAME) as conn:
            cursor = conn.cursor()
            query = "SELECT * FROM Phonebook_data WHERE LOWER(Name) LIKE LOWER(?);"
            search_value = f"%{value}%"
            cursor.execute(query,(search_value,))
            data = cursor.fetchall()

            if data:
                print(f"{'ID':<5} {'Name':<20} {'Phone':<15} {'Address':<25} {'City':<15} {'Pincode':<10}")
                print("-" * 95)
                for id, name, phone, address, city, pincode in data:
                    print(f"{id:<5} {name:<20} {phone:<15} {address:<25} {city:<15} {pincode:<10}")
            
            
                # SELECT ID 
                print("-" * 95)
                select_id = input("Enter ID of Contact you want to Edit: ")

                # NEW_INFORMATION
                name = input("Enter Name: ").strip()
                phone = int(input("Enter Phone Number: "))
                address = input("Enter Address: ").strip()
                city = input("Enter City: ").strip()
                pincode = int(input("Enter Pincode: "))

                update_query = """
                UPDATE Phonebook_data 
                SET Name =?,
                    Phone_no =?, 
                    Address =?, 
                    City =?,
                    Pincode =?
                WHERE ID =?;
                """
                cursor.execute(update_query,(name,phone,address,city,pincode,select_id))
                conn.commit()
                print("\nContact updated successfully!") 
            else:
                print(f"No Record Found with this name: {value}!")
    
    except Exception as e:
        print("ERROR ! Occured:", e)

def delete_contact():
    try:
        value_delete = input("Enter the Name of contact you want to edit ?:  ").lower()

        with sqlite3.connect(DATABASE_NAME) as conn:
            cursor = conn.cursor()
            search_query = """ SELECT * FROM Phonebook_data WHERE LOWER(NAME) LIKE LOWER(?); """
            search_value = f"%{value_delete}%"
            cursor.execute(search_query,(search_value,))
            data = cursor.fetchall()

            if data:
                print(f"{'ID':<5} {'Name':<20} {'Phone':<15} {'Address':<25} {'City':<15} {'Pincode':<10}")
                print("-" * 95)
                for id, name, phone, address, city, pincode in data:
                    print(f"{id:<5} {name:<20} {phone:<15} {address:<25} {city:<15} {pincode:<10}")

                # SELECT ID 
                print("-" * 95)
                select_id = input("Enter ID of Contact you want to Delete: ")

                delete_query = """DELETE FROM Phonebook_data WHERE ID =?;"""
                cursor.execute(delete_query,(select_id,))
                conn.commit()
                print("\nContact deleted successfully")
    
    except Exception as e:
        print("ERROR ! Occured:", e)

            




        

