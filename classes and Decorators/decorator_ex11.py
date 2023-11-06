# circle.py

from time import sleep

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._diameter = None
        self._radius = value

    @property
    def diameter(self):
        if self._diameter is None:
            sleep(0.5)  # Simulate a costly computation
            self._diameter = self._radius * 2
        return self._diameter

circle = Circle(11.0)

print(circle.radius)
print(circle.diameter)
print(circle.diameter)

circle.radius = 100.0
print(circle.radius)
print(circle.diameter)
print(circle.diameter)
