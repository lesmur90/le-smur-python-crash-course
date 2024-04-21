twenty =[]
for value in range(1, 21):
    print(value)

# milli = list(range(1, 1000001))
# for value in range(1, 1000001):
    #print(value)    
# print(milli)

digits = list(range(1, 1000001))

print(min(digits))
print(max(digits))
print(sum(digits))

odd_numbers = list(range(1, 20, 2))
print(odd_numbers)

threes = []
for value in range(3, 31):
    threes.append(value*3)
print(threes)

cubes = []
for value in range(1, 11):
    cubes.append(value**3)
print(cubes)

cubed = [value**3 for value in range(1, 4)]
print(cubed)