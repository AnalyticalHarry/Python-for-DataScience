class Rectangle:
    def __init__(self, length, breadth):
        self._length = length
        self._breadth = breadth

    def _get_length(self):
        return f'Length of rectangle is {self._length}'

    def _change_length(self, value):
        self._length = value
        return f'Now length of rectangle is {self._length}'
        
    def _get_breadth(self):
        return f'Breadth of rectangle is {self._breadth}'

    def _change_breadth(self, value):
        self._breadth = value
        return f'Now breadth of rectangle is {self._breadth}'

    def calculate_area(self):
        return f'Area of rectangle is {self._length * self._breadth}'

obj = Rectangle(5, 10)

length = obj._get_length()
change_length = obj._change_length(7)
breadth = obj._get_breadth()
change_breadth = obj._change_breadth(12)
area = obj.calculate_area()

print(length)
print(change_length)
print(breadth)
print(change_breadth)
print(area)
