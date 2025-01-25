a = 4
tuple_1 = (5, "one", True, 3.14)
print(tuple_1)
print(type(tuple_1))
print(tuple_1[0])
print(tuple_1[1])
print(tuple_1[2])
print(tuple_1[3])

"""#create a new tuple file
tuple_1[1] = 1
print(tuple_1[1])"""
#converting tuple to list
list_a = [5, "one", True, 3.14]
print(type(list_a))

tuple_converting_list = tuple(list_a)
print(tuple_converting_list)
print(type(tuple_converting_list))

#sequence tuple
tuple_2 = tuple(range(5))
print(tuple_2)
print(type(tuple_2))

#combined tuple
tupleA = (1, 2, 3, 4, 5)
tupleB = ("six", "seven", "eight", "nine", "ten")
tupleC = tupleA + tupleB
print(tupleC)

