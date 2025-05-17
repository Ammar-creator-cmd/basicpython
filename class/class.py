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