
phonebook = {
    'Alice' : '703-493-1834',
    'Bob' : '857-384-1234',
    'Elizabeth' : '484-584-2923',
}

# Adding a new entry to the dictionary
phonebook[str(input("Enter name: "))] = str(input("Enter phone number: "))

for key, value in phonebook.items():
    print(key, value)