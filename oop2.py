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
c1 = Circle(21)
c2 = Circle(11)
c3 = Circle(14)
print(c1.area())
c1.print_details()
c2.print_details()