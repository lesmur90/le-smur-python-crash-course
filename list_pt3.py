guests = ['lauren', 'lexie', 'cha', 'duke', 'marv']

# printing with an f-string to include our list with the item of our choosing, according to its index, within a string
print(f"Welcome to dinner, {guests[0].title()}...I love you!")
print(f"Hi {guests[1].title()}, glad you could make it!")
print(f"{guests[2].title()}, welcome to dinner!")
print(f"Big {guests[3].title()}--welcome to dinner my boi!")
print(f"{guests[4].title()}...you was always my dawg...a real one indeed; welcome to dinner my boi!")

# oops...some guest cannot make it to the dinner party, so we who cannot make it first

guests =['lauren', 'lexie', 'cha', 'duke', 'marv']

print(f"Oh no! It looks like {guests[2].title()} cannot make it!!")

# because 'cha' can no longer make it to the dinner, i now must amend the guest list
# i can either use the 'remove' method to remove cha's name...or...i can simply sub her name with another guess by assigning different value to her previously designated index

guests[2] = 'danielle'
print(guests)

# here, i used the insert() method twice to and 'deborah' in the middle of the list, and 'tiz' to the beginning of the list
# i then used the append() method to add 'eddie' to the end of the list
guests.insert(3, 'deborah')
guests.insert(0, 'tiz')
guests.append('eddie')

# created a new variable and used the 'guests' list with each individual index, along with the title() method, as the assigned value 
# to print the guest list as proper nouns, you must assign the 'title()' method to each indivual guest index
updated_guests = guests[0].title(), guests[1].title(), guests[2].title(), guests[3].title(), guests[4].title(), guests[-3].title(), guests[-2].title(), guests[-1].title()
print(f"This our updated list of guests: {updated_guests}")
print("""Hey everyone, I have an update:
      Because our table came in late, I will no longer be able to host everyone;
      I'm going to have to remove a few people from the list.
      Don't be offended; it's nothing personal.
      """)

print(""" Here we go:
""")

# found out the guest table is not large enough, so now i must remove guest down to two
# using the pop method to remove guests from list

removed1 = guests.pop(2)
print(f"1. Sorry {removed1.title()}, we will have to reschedule because our table is not large enough!")

removed2 = guests.pop(6)
print(f"2. {removed2.title()}, you know I love you like a nephew, but our table is too small at the moment! Forgive me bro!")

removed3 = guests.pop(0)
print(f"3. Big {removed3.title()}! You know you my dawg, but we gotta reschedule this thing until we're able to fit everybody!")

removed4 = guests.pop(3)
print(f"4. You know I love you like a brother {removed4.title()}, but we gotta cut ya lol!")

removed5 = guests.pop(2)
print(f"5. Hate to see you go {removed5.title()}, but we'll get back witcha later!")

removed6 = guests.pop(1)
print(f"6. I know how my girl feels about you {removed6.title()}, so we'll make sure we get you over here when we straight!")

print(f"7. You are the love of my life...thank you for being with me {guests[0].title()}. Muah!!!")
print(f"8. Big {guests[1].title()}! You've held me down all month with my new journey into programming. We tight like \"gnat booty\" lol. Welcome bro!")

del guests[1]
del guests[0]
print("""
      """)
print(f"""Current List:
{guests}""")

print("\n")

# creating new, ammeneded list to now implent all of the options for 
guests = ['lauren', 'marv', 'danielle', 'duke', 'deborah', 'tiz', 'lexie', 'eddie']
print("Here is an ammended list of guests:")
print(guests)
print("\n")

# adding an additional guest to the list
guests.append('roni')
print("We added one more guest...a special one from my childhood. This is what we have now:")
print(f"\n\t{guests}")
print("\n")
print("Now, let's see a count of how many we guests we have:")

len(guests) # we find the length of our list by using the 'len()' function
print("\n")
print(len(guests)) # printing the 'len()' displays the legnth of our list in the form of an integer
print("\n")
# now we will swap out a guest by using the 'insert()' method
guests.insert(8, 'tomisha')
print("We have added my childhood friend:")
print(f"{guests}")
print("\n")
print(f"There is no way I could have {guests[8].title()} without adding my cousin {guests[9].title()} to the table.")

guests.append('sydni')
print("\nHere is another variation of the guest list:")
print(guests)

len(guests)
print(f"\nLet's now see how long our guest is now: {len(guests)} people")

guests.pop(10)
print("""\nOh no! Unfortunately, it seems as though our guest list has grown too long!

Here is the new adjusted list:
      """)
print(guests)

print("\nLet's now look at this list in alphabetical order for a sec:")
print("\n", sorted(guests))

print("\nNow let's look at this list in reverse alphabetical order:")
print("\n", sorted(guests, reverse=True))

guests.reverse() # reversing the order of the list by using the 'reverse()' method
print("\nJust for the sake of it, let's take a gander at the reverse order of the original list:")
print("\n", guests)
guests.reverse() # reversing the order back to the original order by using the 'reverse()' method
print("\nNow we're back to our orginial list order:")
print("\n", guests)

# guest_departure = guests[2].title(), guests[4].title(), guests[5].title(), guests[7].title(), guests[8].title(), guests[9].title()>>> # i'm doing away with this variable because of the way it reads when printed...i don't like it
print(f"""Hey {guests[0].title()}, after several phone calls, it looks like 
      {guests[2].title()}
      {guests[4].title()} 
      {guests[5].title()}
      {guests[7].title()}
      {guests[8].title()}
      and {guests[9].title()}
all won't be able to make it to dinner...\n\nNow we're back to our actual original list:""")

# del guest_departure: # doing this didn't remove those members from the list

# del guests[2], guests[4], guests[5], guests[7], guests[8], guests[9] # >>>this command creates a syntax error 'IndexError: list assignment index out of range'

# i had to use negative intergers for the last three names on the list to avoid the previous syntax error
del guests[2], guests[4], guests[5], guests[-3], guests[-2], guests[-1] 

(print("\n", guests))