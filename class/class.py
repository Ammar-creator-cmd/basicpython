class Cat:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def meow(self):
        print("says meow!")

my_cat = Cat("Tom", 5, "Siamese")
print(my_cat)
print(my_cat.name)
print(my_cat.age)
print(my_cat.breed)
my_cat.meow()

friend_cat = Cat("Jerry", 3, "Persian")
print(friend_cat)
print(friend_cat.name)  
print(friend_cat.age)
print(friend_cat.breed)
friend_cat.meow()

class horse:
    species = "Equus ferus caballus" #class variable
    name = None
    def __init__(self, name):
        self.name = name #instance variable

#print(horse.species)

my_horse = horse("Black Beauty")
print(my_horse.name)
print(my_horse.species)

other_horse = horse("Topthorn")
print(other_horse.name)
print(other_horse.species) 

#inheritance
class Car:
    def __init__(self, name, model):
        self.make = name
        self.model = model

    def start(self):
        print(f"{self.make} {self.model} is starting.")

my_Car = Car("Toyota", "Corona")
my_Car.start()

class ElectricCar(Car):
    def __init__(self, name, model):
        super().__init__(name, model)
        self.battery = 100

    def charge(self):
        print(f"{self.make} {self.model} is charging.")
        self.battery = 100
        print(f"Battery charged to {self.battery} %")

my_ElectricCar = ElectricCar("Tesla", "Model T")
my_ElectricCar.start()
my_ElectricCar.charge()
print(my_ElectricCar.battery, "%")
print(my_ElectricCar.make)
print(my_ElectricCar.model)

class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} makes a sound.")
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks.")
class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows.")
class Cow(Animal):
    def speak(self):
        print(f"{self.name} moos.")
class Horse(Animal):
    def speak(self):
        print(f"{self.name} neighs.")
class Sheep(Animal):
    def speak(self):
        print(f"{self.name} bleats.")
class Duck(Animal):
    def speak(self):
        print(f"{self.name} quacks.")
class Chicken(Animal):
    def speak(self):
        print(f"{self.name} clucks.")
class Fish(Animal):
    def speak(self):
        print(f"{self.name} bubbles.")
class Bird(Animal):
    def speak(self):
        print(f"{self.name} chirps.")
class Lion(Animal):
    def speak(self):
        print(f"{self.name} roars.")
my_dog = Dog("Max")
my_cat = Cat("Whiskers")
my_cow = Cow("Rosie")
my_horse = Horse("Joey")
my_sheep = Sheep("Zoey")
my_duck = Duck("Kwack")
my_chicken = Chicken("Goldie")
my_fish = Fish("Nemo")
my_bird = Bird("Robin")
my_lion = Lion("Simba")
my_dog.speak()
my_cat.speak()
my_cow.speak()
my_horse.speak()
my_sheep.speak()
my_duck.speak()
my_chicken.speak()
my_fish.speak()
my_bird.speak()
my_lion.speak()

