import math

def area_of_triangle(base, height):
    return 0.5 * base * height
def perimeter_of_triangle(side1, side2, side3):
    return side1 + side2 + side3

def area_of_square(side):
    return side * side
def perimeter_of_square(side):
    return 4 * side

def area_of_rectangle(length, width):
    return length * width
def perimeter_of_rectangle(length, width):
    return 2 * (length + width)

def area_of_circle(radius):
    return math.pi * radius * radius
def circumference_of_circle(radius):
    return 2 * math.pi * radius

def area_of_semicircle(radius):
    return 0.5 * math.pi * radius * radius
def circumference_of_semicircle(radius):
    return math.pi * radius + 2 * radius

def area_of_rhombus(diagonal1, diagonal2):
    return 0.5 * diagonal1 * diagonal2
def perimeter_of_rhombus(side):
    return 4 * side

def area_of_trapezium(base1, base2, height):
    return 0.5 * (base1 + base2) * height
def perimeter_of_trapezium(base1, base2, side1, side2):
    return base1 + base2 + side1 + side2

print('Hello there, I can find the area and perimeter of any 2D figure.')
print('')
print("To find the area of triangle press 1")
print('To find the area of rectangle press 2')
print('To find the area of a square press 3')
print("To find the area of a circle press 4")
print('To find the area of the semicircle press 5')
print('To find the area of a parallelogram press 6')
print('To find the area of a rhombus press 7')
print('To find the area of a trapezium press 8')
print('')

shape_input = int(input('Enter the number of the shape you want to find the area of: '))

if shape_input == 1:
    base = float(input('Enter the base of the triangle: '))
    height = float(input('Enter the height of the triangle: '))
    print('The area of the triangle is', area_of_triangle(base, height))
    print('The perimeter of the triangle is', perimeter_of_triangle(base, height, height))
elif shape_input == 2:
    length = float(input('Enter the length of the rectangle: '))
    width = float(input('Enter the width of the rectangle: '))
    print('The area of the rectangle is', area_of_rectangle(length, width))
    print('The perimeter of the rectangle is', perimeter_of_rectangle(length, width))
elif shape_input == 3:
    side = float(input('Enter the side of the square: '))
    print('The area of the square is', area_of_square(side))
    print('The perimeter of the square is', perimeter_of_square(side))
elif shape_input == 4:
    radius = float(input('Enter the radius of the circle: '))
    print('The area of the circle is', area_of_circle(radius))
    print('The circumference of the circle is', circumference_of_circle(radius))
elif shape_input == 5:
    radius = float(input('Enter the radius of the semicircle: '))
    print('The area of the semicircle is', area_of_semicircle(radius))
    print('The circumference of the semicircle is', circumference_of_circle(radius) / 2 + 2 * radius)
elif shape_input == 6:
    base = float(input('Enter the base of the parallelogram: '))
    height = float(input('Enter the height of the parallelogram: '))
    print('The area of the parallelogram is', area_of_triangle(base, height))
    print('The perimeter of the parallelogram is', perimeter_of_triangle(base, height, height))
elif shape_input == 7:
    diagonal1 = float(input('Enter the first diagonal of the rhombus: '))
    diagonal2 = float(input('Enter the second diagonal of the rhombus: '))
    print('The area of the rhombus is', area_of_rhombus(diagonal1, diagonal2))
    print('The perimeter of the rhombus is', perimeter_of_rhombus(diagonal1))
elif shape_input == 8:
    base1 = float(input('Enter the first base of the trapezium: '))
    base2 = float(input('Enter the second base of the trapezium: '))
    height = float(input('Enter the height of the trapezium: '))
    print('The area of the trapezium is', area_of_trapezium(base1, base2, height))
    print('The perimeter of the trapezium is', perimeter_of_trapezium(base1, base2, height, height))
else:
    print('Invalid input')