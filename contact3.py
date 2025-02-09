class ContactManager:
    def _init_(self):
        self.contacts = []
    
    def add_contact(self, name, phone, email, address):
        self.contacts.append({"name": name, "phone": phone, "email": email, "address": address})
        print(f"Contact {name} added successfully.")
    
    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return
        for idx, contact in enumerate(self.contacts, 1):
            print(f"{idx}. {contact['name']} - {contact['phone']}")
    
    def search_contact(self, query):
        results = [contact for contact in self.contacts if query in contact["name"] or query in contact["phone"]]
        if results:
            for contact in results:
                print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
        else:
            print("No contact found.")
    
    def update_contact(self, name, phone=None, email=None, address=None):
        for contact in self.contacts:
            if contact["name"] == name:
                if phone:
                    contact["phone"] = phone
                if email:
                    contact["email"] = email
                if address:
                    contact["address"] = address
                print(f"Contact {name} updated successfully.")
                return
        print("Contact not found.")
    
    def delete_contact(self, name):
        for contact in self.contacts:
            if contact["name"] == name:
                self.contacts.remove(contact)
                print(f"Contact {name} deleted successfully.")
                return
        print("Contact not found.")
    
    def run(self):
        while True:
            print("\nContact Manager")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Exit")
            choice = input("Choose an option: ")
            
            if choice == "1":
                name = input("Enter name: ")
                phone = input("Enter phone number: ")
                email = input("Enter email: ")
                address = input("Enter address: ")
                self.add_contact(name, phone, email, address)
            elif choice == "2":
                self.view_contacts()
            elif choice == "3":
                query = input("Enter name or phone number to search: ")
                self.search_contact(query)
            elif choice == "4":
                name = input("Enter name of contact to update: ")
                phone = input("Enter new phone number (leave blank to keep unchanged): ")
                email = input("Enter new email (leave blank to keep unchanged): ")
                address = input("Enter new address (leave blank to keep unchanged): ")
                self.update_contact(name, phone or None, email or None, address or None)
            elif choice == "5":
                name = input("Enter name of contact to delete: ")
                self.delete_contact(name)
            elif choice == "6":
                print("Exiting Contact Manager.")
                break
            else:
                print("Invalid choice. Please try again.")

if _name_ == "_main_":
    manager = ContactManager()
    manager.run()