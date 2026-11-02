# import functions2
# print(functions2.my_function(200, 23.33))
# f2.my_function(100, 22.11)
# from functions2 import my_function, add, addition
# print (my_function(22, 5.0)
# import math
# math.pow(2,2)
# from math import pow
# pow(2,2)
import math

import functions2
# from my_package import shapes
# print(shapes.triangle_area(3,4,5))

from my_package.shapes import triangle_area as area
print(area(3,4,5))

print(dir(math))
print(dir(functions2))

