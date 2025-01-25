"""# replace element

num_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

n = int(input("Enter the number to replace: "))

result = []

#interate over the list
for i in num_list:
    temptuple = list(i)
    result.pop()
    result.append(n)
    result.append(tuple(temptuple))

print("result : {result}")
print("original tuple : {num_list}")"""

# mean of even numbers

num_tuple =(1, 2, 3, 4, 5, 6, 7, 8, 9)

even_sum = 0
even_count = 0

for i in num_tuple:
    if i % 2 == 0:
        even_sum += i
        even_count += 1

print("Sum of even numbers: ", even_sum)
print("Mean of even numbers: ", even_sum / even_count)
