places = ['dubai', 'cape town', 'new zealand', 'italy', 'greece']
print("Here are the places I would like to visit:")
print(places)
print("\n") # printing a new line or "space" between the next line---remember to place '\n' in quotes so that Python will recognize the command

print("Here are the places I'd like to visit (in  temporary order):")
# useed the 'sorted()' method when printing so the list would temporarily be in alphabetical order on the screen
print(sorted(places))
print("\n")

print("Here is my list in its orignal order again:")
print(places)
print("\n")

print(sorted(places, reverse=True)) # the 'sorted()' method allows the 'reverse=True' argument
print("\n")

places.reverse()
print(places)
print("\n")

places.reverse()
print(places)
print("\n")

places.sort()
print(places)
print("\n")

places.sort(reverse=True)
print(places)