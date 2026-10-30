class Circle:
    def __init__(self, r):
        self.radius = r
    def area(self):
        return 22/7 * self.radius**2
    def perimeter(self):
        return 22/7 * self.radius**2
    def print_details(self):
        print("Radius is:",self.radius)
        print("Area:",self.area())
        print("Perimeter is:",self.perimeter())
# object = instance of a class
c1 = Circle(21)
c2 = Circle(11)
c3 = Circle(14)
print(c1.area())
c1.print_details()

my_circles = [c1, c2, c3]
print(my_circles)