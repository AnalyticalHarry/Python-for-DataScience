# List comprehension examples in python programming

# creating squares of numbers between 0 to 20
squares = [ x**2 for x in range(20)]
print(f'squares: {squares}')

# creating a list of even numbers between 0 to 30
even_numbers = [x for x in range(30) if x%2==0]
print(f'even: {even_numbers}')

# creating a lis of odd numbers between 0 to 30
odd_numbers = [x for x in range(30) if x%2 != 0]
print(f'odd: {odd_numbers}')

# creating nested list comprehension 
matrix = [[x for x in range(4) for y in range(3)]]
print(f'matrix: {matrix}')

# using nested list to multiply between mass and acceleration
# mass between 10 to 100 with gap of 10 
mass = [ x for x in range(1, 10, 1)]
acceleration = [ x for x in range(20, 30, 1)]
force = [i*j for i in mass for j in acceleration]
print('force: ', force)

# nested list comprehension
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
c = [[x, y] for x in a for y in b]
print(c)

# multiplying using nested list comprehension
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
c = [11, 12, 13, 14, 15]
d = [x*y*z for x in a for y in b for z in c]
print(f'd: {d}')

# creating a list of negative even number using list comprehension 
neg_even_num = [-x for x in range(20) if x%2==0]
print(f'neg_even_num: {neg_even_num}')
