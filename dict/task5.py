
phonebook = {
    'Alice' : '703-493-1834',
    'Bob' : '857-384-1234',
    'Elizabeth' : '484-584-2923',
}
if str(input("would you like to add a contact to your existing phonebook (yes/no): ")) == 'yes':
    phonebook[str(input("Enter name: "))] = str(input("Enter phone number: "))
else:
    print("No new contact has been added to the existing phonebook")
for key, value in phonebook.items():
    print("the new contact has been uploaded successfully to the existing phonebook")
    print(key, value)
