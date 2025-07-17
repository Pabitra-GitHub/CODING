contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    print("Contact added.")

def view_contacts():
    print("\n--- Contact List ---")
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact['name']} - {contact['phone']}")

def search_contact():
    keyword = input("Search by name or phone: ")
    for contact in contacts:
        if keyword in contact['name'] or keyword in contact['phone']:
            print(contact)
            return
    print("Contact not found.")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    for contact in contacts:
        if contact['name'] == name:
            contact['phone'] = input("Enter new phone: ")
            contact['email'] = input("Enter new email: ")
            contact['address'] = input("Enter new address: ")
            print("Contact updated.")
            return
    print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    for i, contact in enumerate(contacts):
        if contact['name'] == name:
            contacts.pop(i)
            print("Contact deleted.")
            return
    print("Contact not found.")

while True:
    print("\n--- CONTACT BOOK MENU ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        break
    else:
        print("Invalid choice.")
# This code implements a simple contact book application in Python.
# It allows users to add, view, search, update, and delete contacts.
