class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def set_x(self, value):
        self._x = value

    def get_y(self):
        return self._y

    def set_y(self, value):
        self._y = value

# creating an instance of Point
obj = Point(10, 20)

# using the getter to print the value of x
print(obj.get_x())  

# using the setter to update the value of x and then printing the updated value
obj.set_x(40)
print(obj.get_x())  

# using the getter to print the value of y
print(obj.get_y())  

# using the setter to update the value of y. No need to print here since set_y does not return a value.
obj.set_y(50)

# updated value of y
print(obj.get_y()) 
