
def add(a, b, c):
    res = a + b + c
    return res
print(add(9, 7, 5))

def addition( *nums):
    """
     Returns the sum of all the numbers passed as arguments
     parameter:
     integers or floats or mix of integers and floats
     returns:
     sum of numbers(integers or floats)
    """
    total = sum(nums)
    return total
addition(8,8,8)

# call function
print (addition(8,4,5,6,9))
print (addition(1,2,3,4))

def build_profile(**kwargs): #dict key-word args new*
    for k, w in kwargs.items():
        print(f"{k} : {w}")
build_profile(experience=100, name="vee", profession="lawyer", age=19, gender="female")
# function to print 3 functions
def fancy_function(name, *nums, **kwargs):
     print(name)
     print(nums)
     print(kwargs)
# anonymous  = lambda
def square(num):
    return num ** 2
result =square(10)
print(result)

square = lambda num: num*num
print(square(11))

surface_area_cylinder= lambda r, h : 22/7 * r**2 + 22/7 *2 *r * h
print(surface_area_cylinder(14,10))

persons=[
    {"name":"Alex", "age":18, "gender":"male"},
   {"name":"Alvin", "age":20, "gender":"male"},
   {"name":"Bllo", "age":30, "gender":"female"},
   {"name":"Salex", "age":28, "gender":"female"},
]
sorted_by_age = sorted(persons, key=lambda x : x["age"])
print(sorted_by_age)




