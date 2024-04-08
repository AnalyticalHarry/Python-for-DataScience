import math

class Geometry:
    def square_area(self, a):
        # area  = side x side
        return a**2
    
    def rectangle_area(self, w, h):
        # area = width x height
        return w * h
    
    def triangle_area(self, b, h):
        # area = 1/2 x base x height
        return 0.5 * b * h
    
    def regular_polygon_area(self, n, s):
        # area = (number of sides x length of side^2) / (4 x tan(pi / number of sides))
        return (n * s**2) / (4 * math.tan(math.pi / n))
    
    def circle_area(self, r):
        # area = pi x radius^2
        return math.pi * r**2
    
    def ellipse_area(self, a, b):
        # area = pi x radius of long axis x radius of short axis
        return math.pi * a * b
    
    def cube_surface_area(self, a):
        # surface area = 6 x side^2
        return 6 * a**2
    
    def prism_surface_area(self, b, l, h):
        # surface area = 2 x base area + base perimeter x height
        return 2 * b + l * h
    
    def pyramid_surface_area(self, b, l, s):
        # surface area = base area + 1/2 x base perimeter x slant height
        return b + 0.5 * l * s
    
    def sphere_surface_area(self, r):
        # surface area = 4 x pi x radius^2
        return 4 * math.pi * r**2
    
    def cylinder_surface_area(self, r, h):
        # surface area = 2 x pi x radius x (radius + height)
        return 2 * math.pi * r * (r + h)
    
    def cube_volume(self, a):
        # volume = side^3
        return a**3
    
    def prism_volume(self, b, h):
        # volume = base area x height
        return b * h
    
    def pyramid_volume(self, b, h):
        # volume = 1/3 x base area x height
        return (b * h) / 3
    
    def sphere_volume(self, r):
        # volume = 4/3 x pi x radius^3
        return (4/3) * math.pi * r**3
    
    def cylinder_volume(self, r, h):
        # volume = pi x radius^2 x height
        return math.pi * r**2 * h


geometry = Geometry()
# Square
side = 5
print(f"Area of a square with side {side}: {geometry.square_area(side)}")

# Rectangle
width = 10
height = 20
print(f"Area of a rectangle with width {width} and height {height}: {geometry.rectangle_area(width, height)}")

# Triangle
base = 20
height = 15
print(f"Area of a triangle with base {base} and height {height}: {geometry.triangle_area(base, height)}")

# Regular Polygon (Hexagon)
number_of_sides = 6
length_of_side = 15
print(f"Area of a regular hexagon with side length {length_of_side}: {geometry.regular_polygon_area(number_of_sides, length_of_side)}")

# Circle
radius = 7
print(f"Area of a circle with radius {radius}: {geometry.circle_area(radius)}")

# Ellipse
radius_long = 6
radius_short = 4
print(f"Area of an ellipse with major axis {radius_long} and minor axis {radius_short}: {geometry.ellipse_area(radius_long, radius_short)}")

# Cube
side = 3
print(f"Surface area of a cube with side {side}: {geometry.cube_surface_area(side)}")
print(f"Volume of a cube with side {side}: {geometry.cube_volume(side)}")

# Cylinder
radius = 5
height = 10
print(f"Surface area of a cylinder with radius {radius} and height {height}: {geometry.cylinder_surface_area(radius, height)}")
print(f"Volume of a cylinder with radius {radius} and height {height}: {geometry.cylinder_volume(radius, height)}")

# Sphere
radius = 5
print(f"Surface area of a sphere with radius {radius}: {geometry.sphere_surface_area(radius)}")
print(f"Volume of a sphere with radius {radius}: {geometry.sphere_volume(radius)}")

# Prism
base_area = 20
base_perimeter = 60
height = 10
print(f"Surface area of a prism with base area {base_area}, base perimeter {base_perimeter}, and height {height}: {geometry.prism_surface_area(base_area, base_perimeter, height)}")
print(f"Volume of a prism with base area {base_area} and height {height}: {geometry.prism_volume(base_area, height)}")

# Pyramid
base_area = 16
base_perimeter = 16
slant_height = 9
height = 9
print(f"Surface area of a pyramid with base area {base_area}, base perimeter {base_perimeter}, and slant height {slant_height}: {geometry.pyramid_surface_area(base_area, base_perimeter, slant_height)}")
print(f"Volume of a pyramid with base area {base_area} and height {height}: {geometry.pyramid_volume(base_area, height)}")
