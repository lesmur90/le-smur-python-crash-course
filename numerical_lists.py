for value in range(1, 6):
    #print(value)

    numbers = list(range(1, 6))
print(numbers)

range(11)

# start at the value 2, up to the end value 11, adding 2 to each value
even_numbers = list(range(2, 11, 2)) 
print(even_numbers)

# Making a list of the square of each integer from 1 through 10 
squares = []
for value in range(1, 11):
    squares.append(value**2)

print(squares, "\n")

# Simple statistics with a List of Numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(digits, "\n")
print("min digits:", min(digits))

print("max digits:", max(digits))

print("sum digits:", sum(digits), "\n")

# List Comprhensions:
# combines the 'for' loop and the creation of new elements into one line
# and automatically appends each new element
squares = [value**2 for value in range (1, 11)]
print(squares)