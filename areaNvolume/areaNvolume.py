"""import math
r = float(input("Enter the radius of the circle: "))
area = math.pi * r * r
print("the radius of the circle is:", r)
print("pi :", math.pi)
print("The area of the circle is:", round(area, 2))

def volume_of_sphere(r):
    volume = (4/3) * math.pi * r * r * r
    return volume

def surface_area_of_sphere(r):
    surface_area = 4 * math.pi * r * r
    return surface_area

radius = float(input("Enter the radius of the sphere: "))
print("The volume of the sphere is:", round(volume_of_sphere(radius), 2))
print("The surface area of the sphere is:", round(surface_area_of_sphere(radius), 2))"""

import math

def surface_area_of_sphere(r):
    surface_area = 4 * math.pi * r * r
    return surface_area

def volume_of_sphere(r):
    volume = (4/3) * math.pi * r * r * r
    return volume

def surface_area_of_cylinder(r, h):
    surface_area = 2 * math.pi * r * (r + h)
    return surface_area

def volume_of_cylinder(r, h):
    volume = math.pi * r * r * h
    return volume

def surface_area_of_cone(r, l):
    surface_area = math.pi * r * (r + l)
    return surface_area

def volume_of_cone(r, h):
    volume = (1/3) * math.pi * r * r * h
    return volume

print("Choose the shape you want to calculate the area and volume for:")
print("1. Sphere")  
print("2. Cylinder")
print("3. Cone")

choice = int(input("Enter your choice: "))

if choice == 1:
    radius = float(input("Enter the radius of the sphere: "))
    print("The volume of the sphere is:", round(volume_of_sphere(radius), 2))
    print("The surface area of the sphere is:", round(surface_area_of_sphere(radius), 2))
elif choice == 2:
    radius = float(input("Enter the radius of the cylinder: "))
    height = float(input("Enter the height of the cylinder: "))
    print("The volume of the cylinder is:", round(volume_of_cylinder(radius, height), 2))
    print("The surface area of the cylinder is:", round(surface_area_of_cylinder(radius, height), 2))
elif choice == 3:
    radius = float(input("Enter the radius of the cone: "))
    length = float(input("Enter the slant height of the cone: "))
    print("The volume of the cone is:", round(volume_of_cone(radius, length), 2))
    print("The surface area of the cone is:", round(surface_area_of_cone(radius, length), 2))
else:
    print("Invalid choice")
