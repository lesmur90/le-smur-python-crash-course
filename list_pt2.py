sudans = ['honda', 'ford', 'nissan']
print(sudans)

# the 'pop()' method allows you to use the value of an item after you have removed it from a list
popped_sudans = sudans.pop()

# printing the list after assigning the 'pop' method allows you to the list without the removed item
print(sudans)

# printing the 'popped' variable allows you to confirm exactly what was removed from the list
print(popped_sudans)

# it is important to remember that, when working with multiple lines of code, to re-state your list when using the '.pop' method is a value of a variable after using it previously. if you don't, it will simply 'pop' the next item in the list

sudans = ['honda', 'ford', 'nisson']
last_owned = sudans.pop()
print(f"The last stick shift we owned was a brown 1984 {last_owned.title()} Maxima!!")

# you can use the pop() to remove an item from any position in a list by including the index of the item you want to remove in parentheses

sudans =['honda', 'ford', 'nissan']
second_owned = sudans.pop(1)
never_owned = sudans.pop(0)
print(f"The second vehicle that we owned was a baby blue 1998 {second_owned.title()} Taures.")

# Sometimes when you don't know the position of the value you want to remove from a list
# If you only know the value of the item you want to remove, you can use the remove() method

sudans = ['honda', 'ford', 'nissan']
print(sudans)

sudans.remove('nissan')
print(sudans)

# you can also use the remove() method to work with a value that's being removed from a list
# we will now remove the value 'nissan' and print a reason for removing it from the list

sudans = ['hond', 'ford', 'nissan']
print(sudans)

too_old = 'nissan'
sudans.remove(too_old)
print(sudans)
print(f"\nI like driving stick shifts a lot, but that 19984 {too_old.title()} was too old!!")