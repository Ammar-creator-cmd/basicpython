import math #some common mathematical function
"""
x = int(input("enter a number: "))
square_root = math.sqrt(x)
print("The square root of", x, "is", square_root)

base = 2
exponent = 3
result = math.pow(base, exponent)
print("base", base, "index", exponent, "is", result)

absolute = math.fabs(-5)
print("The absolute value of -5 is", absolute) #fabs = floating point absolute value

floor_value = math.floor(5.9)
print("The floor value of 5.9 is", floor_value) #the value rounds down (floor = floors)

ceil_value = math.ceil(5.1)
print("The ceil value of 5.1 is", ceil_value) #the value rounds up (ceil = ceilings)

round_value = round(5.5)
print("The round value of 5.5 is", round_value) #the value rounds to the nearest integer 
"""

#calculator
def subtract(x, y):
    print(f"\nThe result of {x} - {y} is {x - y}")

def add(x, y):
    print(f"\nThe result of {x} + {y} is {x + y}")


def multiply(x, y):
    print(f"\nThe result of {x} x {y} is {x * y}")

def divide(x, y):
    print(f"\nThe result of {x} / {y} is {x / y}")

print("Available operations:")
print("1 = Add")
print("2 = Subtract")
print("3 = Multiply")
print("4 = Divide")

choice = input("Enter operations (1/2/3/4): ")

if choice == "1":
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    add(x, y)
elif choice == "2":
    x = int(input("Enter the subtsracted number: "))
    y = int(input("Enter the substracting number: "))
    subtract(x, y)
elif choice == "3":
    x = int(input("Enter the first number: "))
    y = int(input("Enter the multiplyer number: "))
    multiply(x, y)
elif choice == "4":
    x = int(input("Enter the divided number: "))
    y = int(input("Enter the dividing number: "))
    divide(x, y)
else:
    print("Invalid input")
