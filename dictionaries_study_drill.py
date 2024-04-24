# using a dictionary to store basic informationa bout a person
girlfriend = {'first_name': 'lauren','last_name': 'davis', 
              'age': 39, 'city': 'takoma park'}

print(girlfriend['first_name'].title())
print(girlfriend['last_name'].title())
print(girlfriend['age'])
print(girlfriend['city'].title())

# using a dictionary to store the favorite numbers of people
favorite_numbers = {'michael jordan': 23, 'kobe bryant': 24, 'steph curry': 30,
                    'klay thompson': 11, 'magic johnson': 32}

#for favorite_number in favorite_numbers:
    #print(favorite_number.title())

# tried using a loop to print the key and value, but that didn't work 
# it only printed the key

print(favorite_numbers['michael jordan'])
print(favorite_numbers['kobe bryant'])
print(favorite_numbers['steph curry'])
print(favorite_numbers['klay thompson'])
print(favorite_numbers['magic johnson'])

# creating a python glossary using a dictionary

glossary = {
    'variable': 'symobolic name for a value',
    'string': 'a sequence of characters enclosed in quotaton marks',
    'boolean expression': 'a statement that determines either true or false',
    'list': 'a data structure to store a collection of items',
    'loop': 'programming construct that allows you to repeatedly execute '
            'a block of code\nuntil a specified condion is met',
    'if statement': 'a control structure in programming that allows you to '
            'execute certain code\nbased on whether a condition is '
            'true of false',             
    }
 # creating new variables to store the keys for cleaner print() calls
gloss1 = glossary['variable'].title()
gloss2 = glossary['string'].title()
gloss3 = glossary['boolean expression'].title()
gloss4 = glossary['list'].title()
gloss5 = glossary['loop'].title()
gloss6 = glossary['if statement'].title()

print(f"\nVariable:\n\t{gloss1}\n")
print(f"String:\n\n\t{gloss2}:\n")
print(f"Boolean Expression:\n\n\t{gloss3}:\n")
print(f"List:\n\n\t{gloss4}:\n")
print(f"Loop:\n\n\t{gloss5}:\n")
print(f"If Statement:\n\n\t{gloss6}:\n")

# looping through the numbers dictionary using a for loop
# this is ref back to the comment in line 16
# 'key' and 'value' and be abbreviated in a for loop by using 'k' & 'v'
for k, v in favorite_numbers.items():
    print(f"Name: {k.title()}") # must maintain 'k' versus using 'key'
    print(f"Jersey No: {v}\n") # must maintain 'v' versus using 'value'

# bonus for a refresher
bucks = []
for value in range(1, 1001):
    print(f"${value}")

# looping through a dictionary in alphabetical order
# to loop through both key and value, use the 'item()' method.
# to loop only through the name/key, use the 'key()' method.
for name, number in sorted(favorite_numbers.items()):
    print(f"{name.title()} is one of my favorite players ever. " 
          f"He wore number {number}.\n")

# looping through all the values of my dictionary
print("These are the numbers that my favorite players have worn:\n")
for number in favorite_numbers.values():
    if number == 23:
        print(f"No. {number} (Jordan)")
    else:
        print(f"No. {number}")

# some of my favorite players wore the same number
players = {
    'michael jordan': 23, 
    'kobe bryant': 24, 
    'allen iverson': 3,
    'steph curry': 30,
    'shaq': 32,
    'magic johnson': 32,
    'larry bird': 33,
    }

# using 'set()' method to avoid repetitive values
print("\nSome of my favorite plyers wore these numbers:\n")
for number in set(players.values()):
    print("\t", number)

# checking if 'lebron james' is in my dictionary using an if statement
if players != 'lebron james':
    print("\nThough LeBron James wore no. 23, "
         "he is not one of my favorite players.\n")
    
# adding a key and value to my dictionary
players['klay thompson'] = 11

# using a loop to print players name
for name in sorted(players.keys()): 
    if name == 'michael jordan':
        print(name.title(), "(The G.O.A.T.)")
    else: 
        print(name.title())

# cleaning up code from line 27 using a 'for' loop to print glossary
print("\nOn another note, I used some cleaner code (less print calls) "
      "to execute the same output as line 27, using a 'for' loop." 
      "\nHow cool is that?!"
      "\nCheck it out!: ")

# way less print calls than line before, creating cleaner code in less lines
for k, v in glossary.items():
    print(f"\n{k.title()}:\n")
    print(f"- {v}\n")