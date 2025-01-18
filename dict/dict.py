dict_a = {
    'name': 'Ammar',
    'age': 12,
}
print(dict_a['name'])
print(dict_a['age'])\

#member ship check
result =  'name' in dict_a
print(result)

#no duplicate key
dict_b = {
    1: 'Apik',
    2: 'agus',
    3: 'Apik',
    4: 'ancor',
}
print(dict_b)
print("length of dict_b",len(dict_b))
print("keys", dict_b.keys())
print("values", dict_b.values())
print("items", dict_b.items())

print("#"*12)
print("interating over dict_b")
print("")
for key in dict_b.keys():
    print(key)
print("")
for value in dict_b.values():
    print(value)
print("")
for key, value in dict_b.items():
    print(key, value)
print("")
for i in dict_b:
    name = dict_b[i]
    print(name)

#item method
print()
print("item method")
for key, value in dict_b.items():
    print(key, value)