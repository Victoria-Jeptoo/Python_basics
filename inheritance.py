from encodings import ptcp154


class Employee:
    def __init__(self, name, email, department, salary):
        self.name = name
        self.email = email
        self.department = department
        self.salary = salary

    def show_details(self):
        print(self.name, self.department, self.salary)


class PermanentEmployee(Employee):
    def __init__(self, name, email, department, salary, cover, increment):
        super().__init__(name, email, department, salary)
        self.cover = cover
        self.increment = increment


class ContractEmployee(Employee):
    def __init__(self, name, email, department, salary, tenure):
        super().__init__(name, email, department, salary)
        self.tenure = tenure


p1 = PermanentEmployee("Jane Mark", "jm@yahoo.com", "HR", 100_00, "Britam","4")
c1 = ContractEmployee("Jin Jan", "jj@yahoo.com", "Sales", 88_000, 3)

p1.show_details()
c1.show_details()

# TODO overriding

