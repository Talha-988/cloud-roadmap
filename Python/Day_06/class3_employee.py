class Employee:
    company_name= "Redixcode"
    def __init__(self, name,department,salary):
        self.name=name
        self.department=department
        self.salary=salary

    def display(self):
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Salary: {self.salary}")
e1 = Employee("Talha","Cloud",80000)
e2 = Employee("Ali","DevOps",90000)
print("Company:",Employee.company_name)
e1.display()
print("-" * 20)
e2.display()