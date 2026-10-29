# class - blueprint for creating an object
from unittest import result


class Persom:
#constructor - initialize an object
  def __init__(self, name, dob, age, weight, height):
    self.name=name
    self.dob=dob
    self.age=age
    self.weight=weight
    self.height=height
  def display(self):
      print(f"Name is {self.name} and dob is {self.dob}")
  def get_bmi(self):
     result =self.weight/(self.height**2)
     return result


p1= Persom(  "Hun Chink",  "08-09-7890", 89, 70, 1.87)
p2= Persom( "Vee Wanja", "31-09-3089", 56, 67, 1.56)
p1.display()
p2.display()
print(f"{p1.name} bmi is {p1.get_bmi()}")
print(f"{p2.name} bmi is {p2.get_bmi()}")