class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._update_area()

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value
        self._update_area()

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
        self._update_area()

    def _update_area(self):
        self._area = self._width * self._height

    @property
    def area(self):
        return self._area


rect = Rectangle(10, 5)
area_initial = rect.area

# changing the width of the rectangle
rect.width = 20

# Accessing the area again after changing the width
area_after_width_change = rect.area

# changing the height of the rectangle
rect.height = 10

# area again after changing the height
area_after_height_change = rect.area

(area_initial, area_after_width_change, area_after_height_change)
