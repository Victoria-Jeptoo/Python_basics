#if else
import os

names= "Jake"
age = 19
if age >= 18:
    print("Adult")
else:
    print("Child")

name = input("What's  your name> ")
age= input("Enter  your age: ")
if not age.isnumeric():
    print('invalid age')
 # terminate
    os._exit(0)
if  int(age) > 18:
    print(name +" " + "is an adult")
else:
    print(name +" "+ "is a child")

# lists, booleans, tuples, dictionary