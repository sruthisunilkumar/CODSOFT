class Contact:
    def _init_(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def _init_(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully.")

    def view_contacts(self):
        if self.contacts:
            print("Contact List:")
            for contact in self.contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone_number}")
        else:
            print("No contacts in the list.")

    def search_contact(self, keyword):
        found_contacts = []
        for contact in self.contacts:
            if keyword.lower() in contact.name.lower() or keyword in contact.phone_number:
                found_contacts.append(contact)
        return found_contacts

    def update_contact(self, name, new_contact):
        for i, contact in enumerate(self.contacts):
            if contact.name == name:
                self.contacts[i] = new_contact
                print("Contact updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self, name):
        for i, contact in enumerate(self.contacts):
            if contact.name == name:
                del self.contacts[i]
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone_number, email, address)
            contact_book.add_contact(new_contact)
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            keyword = input("Enter name or phone number to search: ")
            found_contacts = contact_book.search_contact(keyword)
            if found_contacts:
                print("Found contacts:")
                for contact in found_contacts:
                    print(f"Name: {contact.name}, Phone: {contact.phone_number}")
            else:
                print("No matching contacts found.")
        elif choice == '4':
            name = input("Enter name of contact to update: ")
            new_name = input("Enter new name: ")
            phone_number = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            new_contact = Contact(new_name, phone_number, email, address)
            contact_book.update_contact(name, new_contact)
        elif choice == '5':
            name = input("Enter name of contact to delete: ")
            contact_book.delete_contact(name)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

