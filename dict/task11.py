def add_contacts():
    contacts = {}

    num_contacts = int(input("How many contacts would you like to save? "))

    for _ in range(num_contacts):
        name = input("Enter the name: ")
        contact = input("Enter the contact: ")
        contacts[name] = contact
    
    return contacts

def display_contacts(contacts):
    print("\nContact Book:")
    for name, contact in contacts.items():
        print(f"Name: {name}, Contact: {contact}")

def main():
    contacts = add_contacts()
    display_contacts(contacts)

if __name__ == "__main__":
    main()