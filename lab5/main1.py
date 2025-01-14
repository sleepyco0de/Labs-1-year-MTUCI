class Circle:

    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return 'Radius {}'.format(self.radius)

    def set_radius(self, new_radius):
        self.radius = new_radius
        return "Radius edit {}".format(self.radius)

krug = Circle(5)
print(krug.get_radius())
print(krug.set_radius(56))
print(krug.get_radius())
