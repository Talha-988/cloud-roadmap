class Animal:
    def __init__(self,name):
        self.name = name
class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed
a1 = Dog("Tommy","German Shepard")
print(a1.name)
print(a1.breed)
