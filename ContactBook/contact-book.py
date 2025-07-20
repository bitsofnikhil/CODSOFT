contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    contacts[name] = phone
    print("Contact saved.")

def view_contacts():
    print("\nContact Book:")
    for name, phone in contacts.items():
        print(f"{name} → {phone}")

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"{name} → {contacts[name]}")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Name not found.")

while True:
    print("\n1. Add  2. View  3. Search  4. Delete  5. Exit")
    choice = input("Choose option: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        break
    else:
        print("Invalid choice.")
