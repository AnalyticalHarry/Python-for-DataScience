# Example 1 : Add !
super_hero = ["Superman", "Batman", "Homelander"]

# for loop
for i in range(len(super_hero)):
    super_hero[i] = super_hero[i] + "!"
print(super_hero)

# list comprehnsion 
super_hero = [x + "!" for x in super_hero]
print(super_hero)

# Example 2 : Replace
super_hero = ["Superman", "Batman", "Homelander"]
# for loop
for i in range(len(super_hero)):
    super_hero[i] = super_hero[i].replace("man", "person")
print(super_hero)

# list comprehnsion 
super_hero = [x.replace("man", "person") for x in super_hero]
print(super_hero)

# Example 3 : Upper Case
super_hero = ["Superman", "Batman", "Homelander"]
for i in range(len(super_hero)):
    super_hero[i] = super_hero[i].upper()
print(super_hero)

# list comprehnsion 
super_hero = [x.upper() for x in super_hero]
print(super_hero)


# Example 4 : Reverse String
super_hero = ["Superman", "Batman", "Homelander"]
for i in range(len(super_hero)):
    super_hero[i] = super_hero[i][::-1]
print(super_hero)

super_hero = [x[::-1] for x in ["Superman", "Batman", "Homelander"]]
print(super_hero)

# Example 5 : Add length of string
super_hero = ["Superman", "Batman", "Homelander"]
for i in range(len(super_hero)):
    super_hero[i] = super_hero[i] + str(len(super_hero[i]))
print(super_hero)

super_hero = [x + str(len(x)) for x in ["Superman", "Batman", "Homelander"]]
print(super_hero)

# Example 6 : Add length of string with tuple
super_hero = ["Superman", "Batman", "Homelander"]
super_hero_with_length = []
for name in super_hero:
    super_hero_with_length.append((name, len(name)))
print(super_hero_with_length)

super_hero_with_length = [(x, len(x)) for x in ["Superman", "Batman", "Homelander"]]
print(super_hero_with_length)

# Example 7 : Filter
super_hero = ["Superman", "Batman", "Homelander", "Wonder Woman"]
filtered_heroes = []
for name in super_hero:
    if 'man' in name.lower():
        filtered_heroes.append(name)
print(filtered_heroes)

filtered_heroes = [x for x in ["Superman", "Batman", "Homelander", "Wonder Woman"] if 'man' in x.lower()]
print(filtered_heroes)

