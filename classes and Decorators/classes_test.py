# Class example
class Rectangle:
    def __init__(self, length:int, breadth:int) -> None:
        self.length = length
        self.breadth = breadth
    @property
    def length(self):
         print("Getting Length")
         return self._length
    @property
    def breadth(self):
         print("Getting breadth")
         return self._breadth
    @length.getter
    def length(self, length) -> None:
        print(f'Setting Length {length}')
        self._length, length
        self._area = 0
        self._circumference = 0
    @breadth.getter
    def breadth(self, breadth) -> None:
        print(f'Setting breadth {breadth}')
        self._breadth, breadth
        self._area = 0
        self._circumference = 0
    @property
    def area(self) -> int:
        self._area = self._length * self._breadth
        return self._area 
    @property
    def circumference(self) -> int:
            self._circumference = (2 * self._length) + (2 * self._breadth)
            return self._circumference
    def check_square(self) -> bool:
        return True if self._length == self._breadth else False

rect = Rectangle(10, 11) 
print(f'{rect.length}')
print(rect._area)
print(rect.area())
print(rect.circumference())
rect.breadth = 11 
rect1 = Rectangle(23,23.5)
print(f'(length, breadth) : {rect1.breadth}')
print(rect1.area())
print(rect1.circumference())