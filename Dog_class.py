class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

        print(f"\n{self.name} is {self.age} years' old")

    def sit(self):
        
        print(f"{self.name} is sitting")

    def rollover(self):

        print(f"{self.name} rolled over")

my_dog = Dog("Wille", 16)
your_dog = Dog("Lucy", 10)
my_dog.sit()
my_dog.rollover()

