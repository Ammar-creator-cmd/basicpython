number_of_profiles = int(input("enter the number of profiles:" ))

profiles = []
for i in range(number_of_profiles):
    name = input("enter the name: ")
    password = input("enter the passwords: ")
    profiles.append((name, password))
print(profiles)
