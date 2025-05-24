class Shape:
    def __init__(self, name, radius=0):
        self.name = name
        self.radius = radius
    def draw(self):
        print(f"Drawing {self.name} at radius {self.radius} degrees")

circle = Shape("Circle", 45)
circle.draw()

class rectangle(Shape):
    def __init__(self, name, height, width):
        super().__init__(name)
        self.height = height
        self.width = width
    def drawRect(self):
        print(f"Drawing {self.name} at dimensions of {self.height} units x {self.width} units")
    def area(self):
        return self.height * self.width
rectangle1 = rectangle("Rectangle", 20, 30)
rectangle1.drawRect()
rectangle1.draw()
print(f"Area of {rectangle1.name} is {rectangle1.area()} units")
rect2 = rectangle("Rectangle2", 10, 20)
rect2.drawRect()
rect2.draw()
print(f"Area of {rect2.name} is {rect2.area()} units")

class human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def speak(self):
        print(f"{self.name} greets you!")
    def info(self):
        print(f"{self.name} is {self.age} years old.")

class woman(human):
    def __init__(self, name, age, hair_color,):
        super().__init__(name, age)
        self.hair_color = hair_color
    def speak(self):
        print(f"{self.name} says hello!")
    def info(self):
        print(f"{self.name} is {self.age} years old and has {self.hair_color} hair.")

class man(human):
    def __init__(self, name, age, hair_color):
        super().__init__(name, age)
        self.hair_color = hair_color
    def speak(self):
        print(f"{self.name} says hey!")
    def info(self):
        print(f"{self.name} is {self.age} years old and has {self.hair_color} hair.")
def main():
    man1 = man("John", 20, "brown")
    woman1 = woman("Zoe", 15, "blonde")
    woman1.speak()
    woman1.info()
    man1.speak()
    man1.info()


if __name__ == "__main__":
    main()
