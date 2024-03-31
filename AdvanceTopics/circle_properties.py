import math

class Circle:
    def __init__(self, radius):
        self._radius = radius

    def _get_radius(self):
        print("Get radius")
        # Check if _radius is defined before returning it
        if hasattr(self, '_radius'):
            return self._radius
        else:
            return "Radius not set" 

    def _set_radius(self, value):
        print("Set radius")
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    def _del_radius(self):
        print("Delete radius")
        # Use del to delete the attribute, assuming it exists
        if hasattr(self, '_radius'):
            del self._radius
    def calculate_area(self):
        # method calculates and returns the area of the circle.
        if hasattr(self, '_radius'):
            return math.pi * self._radius ** 2
        else:
            return "Radius not set or deleted, cannot calculate area."
            
    radius = property(
        fget=_get_radius,
        fset=_set_radius,
        fdel=_del_radius,
        doc="The radius property."
    )

obj = Circle(10)
print(obj)
print(obj._get_radius())

# setting radius to 20
obj._set_radius(20)
print(obj._get_radius())

# delete radius 
obj._del_radius()
print(obj._get_radius())

# calculating area
obj._set_radius(50)
print(obj.calculate_area())
