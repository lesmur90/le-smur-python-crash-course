#age = 19
#if age >= 18:
    #print("You are old enough to vote!")
   # print("Have you registered to vote yet?")
age = 17

if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

# the 'if-elif-else' chain
# the following example consists of admission fees for different ages
age = 12

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

# a more efficient and consise way to run the same code would be:
age = 11

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"Your admission cost is ${price}.")

# using multiple 'elif' blocks
age = 66

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"Your admission cost is ${price}.\n")

# 'else' block is not required at the end of 'if-elif-else' chain
# the last line could have looked like the following:
# elif age >= 65:
#     price = 20

# 'if-elif-else' chain is only appropiate when only one test needs pass
# when more than one condition could be true, use multi 'if' statements
# using a pizza topping example w/multi simple 'if' statements

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nYour pizza is done!")




