from Database import database

def add_contact():
    print("\n---Add--New--Contact---")
    name = input("Enter Name: ").strip()
    phone = int(input("Enter Phone Number: "))
    address = input("Enter Address: ").strip()
    city = input("Enter City: ").strip()
    pincode = int(input("Enter Pincode: "))
    database.insert_contact(name, phone, address, city, pincode)

def add_multiple_contacts():
    pass

def search_contact():
    pass

def edit_contact():
    pass

def delete_contact():
    pass

def delete_all():
    pass

def main():
    database.init_database()
    while True:
        print("----------------------------")
        print("_____Phonebook__Manager_____")
        print("----------------------------")
        print("1. Add Contact")
        print("2. Add Multiple Contacts")
        print("3. Search Contact")
        print("4. Edit Contact")
        print("5. Delete Contact")
        print("6. Delete all")
        print("7. Exit")
        choice = input("Select Options.. ")
        match choice:
            case "1":
                add_contact()
            case "2":
                add_multiple_contacts()
            case "3":
                search_contact()
            case "4":
                edit_contact()
            case "5":
                delete_contact()
            case "6":
                delete_all()
            case "7":
                break
            case _:
                print("Invalid Choice..")
        


if __name__=="__main__":
    main()