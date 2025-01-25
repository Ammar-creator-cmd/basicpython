numbers = input("Enter a list of numbers separated by space: ")
numbers_list = numbers.split()
numbers_list = [int(num) for num in numbers_list]
print("The list of numbers is:", numbers_list)
even_list = [num for num in numbers_list if num % 2 == 0]
print("The list of even numbers is:", even_list)