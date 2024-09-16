
odd_numbers = list(range(3, 30, 3))
for odd_number in odd_numbers:
    print(odd_number)

cubes = []

for value in range(1, 11):
    cube = value**3
    cubes.append(cube)
print(cubes)

cubes = [value**3 for value in range(1, 16)]
print(cubes)