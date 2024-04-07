# we can store containers in containers 
# which mean we can store list inside list

# creating list of numbers
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
c = [11, 12, 13, 14, 15]
d = [16, 17, 18, 19, 20]

#c creeating a list inside list
container = [[a], [b], [[c], [d]]]

print(container)
print(container[0])
print(container[1])
print(container[2)

# first list
for i in range(len(container[0])):
    print(container[0][i])

# second list
for i in range(len(container[1])):
    print(container[1][i])

# third list 
for i in range(len(container[2])):
    print(container[2][i])

for i in range(len(container[2][0])):
    print(container[2][0][i])

for i in range(len(container[2][1])):
    print(container[2][1][i])

# elements of the first list directly
for item in container[0][0]:  # container[0] is [a], container[0][0] is a
    print(item)

# elements of the second list directly
for item in container[1][0]:  # container[1] is [b], container[1][0] is b
    print(item)

# elements of the nested lists (c and d) inside the third list
for subcontainer in container[2]:  # container[2] is [[c], [d]]
    for item in subcontainer[0]:  # subcontainer[0] is c or d
        print(item)
