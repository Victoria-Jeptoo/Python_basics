# bank acc == owner, acc no, balance, history 1999-08-28
from datetime import date, datetime

class Client:
    def __init__(self, names:str, kra_pin:str, dob:str, gender:str):
        self.names = names
        self.kra_pin = kra_pin
        self.dob = dob
        self.gender = gender

    def print_details(self):
        print(self.names)
        print(self.kra_pin)

    def calc_age(self):
        today = date.today()
        birth_date = datetime.strptime(self.dob, "%Y-%m-%d")
        ages = today.year - birth_date.year
        return ages

class BankAccount:
    def __init__(self, owner, acc_no, balance):
        self.owner = owner
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += abs(amount)

    def withdraw(self, amount :int):
        if amount > self.balance:
            print("Not enough money")
        else:
            self.balance -= abs(amount)

    def print_details(self):
        print(self.owner.names)
        print(self.acc_no)
        print(self.balance)
        print("-----------------")


Jane = Client("Jane Mwangi", "A001", "1999-01-16", "F")
Allan = Client("Allan Koech", "A002", "2003-01-19", "M")

acc1 = BankAccount(Jane, "11111", 700000)
acc2 = BankAccount(Jane, "22222", 800000)
acc3 = BankAccount(Allan, "33333", 900_000_289)

acc1.deposit(10_000)
acc1.withdraw(3000)
acc1.print_details()
acc1.withdraw(15_000)
acc1.print_details()
print("Jane's age:", Jane.calc_age())
print("Allan's age:", Allan.calc_age())

print(acc1.owner.names, acc1.owner.calc_age())
print(Allan.names, Allan.calc_age())

# dob = "2004-01-12"
# today = date.today()
# print(f"{today.year}-/-{ today.month}-/-{today.day}")
# convert string to date
# birth_date = datetime.strptime(dob, "%Y-%m-%d")
# ages = today.year - birth_date.year
# print(ages)


