
def add_contact(phoneBook):
    name = input("Enter a contact name: ")
    number = input("Enter a contact number: ")
    if name in phoneBook:
        print(f"{name} already exists in the phone book.")
    else:
        phoneBook[name] = number
        print(f"{name} added to the phone book.")

def search_contact(phoneBook):
    name = input("Enter contact name to search: ")
    if name in phoneBook:
        print(f"{name}: {phoneBook[name]}")
    else:
        print(f"{name} not found in the phone book.")

def display_contacts(phoneBook):
    if phoneBook:
        print("\nContact List:")
        for name, number in phoneBook.items():
            print(f"{name}: {number}")
    else:
        print("Phone book is empty.")

def delete_contact(phoneBook):
    name = input("Enter contact name to delete: ")
    if name in phoneBook:
        del phoneBook[name]
        print(f"{name} deleted successfully from the phone book.")
    else:
        print(f"{name} not found in the phone book.")

if __name__ == "__main__":
    phoneBook = {}
    while True:
        print("\nPhonebook Menu")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. Display Contacts")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_contact(phoneBook)
        elif choice == "2":
            search_contact(phoneBook)
        elif choice == "3":
            delete_contact(phoneBook)
        elif choice == "4":
            display_contacts(phoneBook)
        elif choice == "5":
            print("Exiting phone book. Goodbye!")
            break
        else:
            print("Invalid choice, please enter a number between 1 and 5.")