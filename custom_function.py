
import math

def greet():
    print("Hello")

def greeting(name):
    print(f"Hello {name}")

# Calling functions
# greet()
greeting("Sila")
greeting("Samila")
greeting("Ahmed")


def volume_cylinder_better(radius, height):
    volume = math.pi * radius**2 * height
    area = 2 * math.pi * radius * (radius + height)
    return volume, area


volume, area = volume_cylinder_better(10, 20)
print(f"Volume is {volume:.3f} and area is {area:.3f}")

v, a = volume_cylinder_better(height=20, radius=10)
print(f"Volume is {v:.3f} and area is {a:.3f}")


def divide(a, b, should_round=False):
    result = a / b

    if should_round == True:
        return round(result, 2)
    else:
        return result


print(divide(9, 5.11, should_round=True))
print(divide(20, 3, should_round=True))

print(round(20.667, 2))
