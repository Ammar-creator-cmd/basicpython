import math

def volume_of_rectangular_prism(length, width, height):
    return length * width * height

def surface_area_of_rectangular_prism(length, width, height):
    return 2 * (length * width + width * height + height * length)

def volume_of_triangular_prism(base, height, length):
    return 0.5 * base * height * length

def surface_area_of_triangular_prism(base, height, length):
    base_area = 0.5 * base * height
    side_area1 = base * length
    side_area2 = height * length
    hypotenuse = math.sqrt(base**2 + height**2)
    side_area3 = hypotenuse * length
    return 2 * base_area + side_area1 + side_area2 + side_area3

print("Shapes available to calculate the volume and surface area of: ")
print("1. Rectangular Prism")
print("2. Triangular Prism")
choice = int(input("Enter your choice: "))

if choice == 1:
    length = float(input("Enter the length of the prism: "))
    width = float(input("Enter the width of the prism: "))
    height = float(input("Enter the height of the prism: "))
    print("The volume of the rectangular prism is", volume_of_rectangular_prism(length, width, height))
    print("The surface area of the rectangular prism is", surface_area_of_rectangular_prism(length, width, height))
elif choice == 2:
    base = float(input("Enter the base of the prism: "))
    height = float(input("Enter the height of the prism: "))
    length = float(input("Enter the length of the prism: "))
    print("The volume of the triangular prism is", volume_of_triangular_prism(base, height, length))
    print("The surface area of the triangular prism is", surface_area_of_triangular_prism(base, height, length))
else:
    print("Invalid input")