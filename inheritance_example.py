class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and my color is {self.color}")

class Dog(Pet):
    def __init__(self, name, age):
        super().__init__(name, age)

    def speak(self):
        print("Bark")

class Fish(Pet):
    pass

p = Pet("milo", 5)
p.show()

c=Cat("percy", 7, "grey")
c.show()
c.speak()

d=Dog("spot", 9)
d.show()
d.speak()

f=Fish("fishy", 2)
f.show()

