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
    print("\n---Add--Multiple--Contacts---")
    try:
        nums = int(input("Enter the numbers how many contacts do you want to add?: "))

        for i in range(1, nums+1):
            add_contact()
    except:
        print("Invalid input Please ebter only numbers.")

def view_all():
    database.view()

# def search_contact():
#     name = input("Enter name to search the contact?: ")


def edit_contact():
    pass

def delete_contact():
    pass

def delete_all():
    print("\n---Delete--All--Contacts---")
    
    user_input = input("Are you sure to Delete all Contacts (yes/no)?" ).casefold()

    if user_input.strip() == "yes":
        user_input2 = input("Are sure you can't restore once action done..(yes/no)?" ).casefold()
        if user_input2.strip() == "yes":
            print("All Contacts Deleted")
            database.delete_all()
        else:
            print("Invalid Input")
    else:
        print("Invalid Input Please Enter only Yes or No..")
               
    


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
        print("7. View all")
        print("8. Exit")
        choice = input("Select Options.. ")
        match choice:
            case "1":
                add_contact()
            case "2":
                add_multiple_contacts()
            case "3":
                database.search_contact()
            case "4":
                edit_contact()
            case "5":
                delete_contact()
            case "6":
                delete_all()
            case "7":
                view_all()
            case "8":
                break
            case _:
                print("Invalid Choice..")
        


if __name__=="__main__":
    main()