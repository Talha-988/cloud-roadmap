class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
class Student(Person):
    def __init__(self,name,age,rollno):
        super().__init__(name,age)
        self.rollno = rollno
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Roll no: {self.rollno}")

s = Student("Talha",20,101)
s.display()