#alien_color = 'green'
#if alien_color == 'green':
    #print("5 points!")

# writing a test that fails the conditions
#alien_color = 'yellow'
#if alien_color == 'red':
    #print("15 points!")
#if alien_color == 'yellow':
    #print("10 points!")

# writing if-else chain
alien_color = 'red'

if alien_color == 'red':
    print("\n15 points!\n")
else:
    print("5 points")

# if-elif-else chain

alien_color = 'green' # test for green ('if')
if alien_color == 'green':
    print("You've earned 5 points!")
elif alien_color == 'yellow':
    print("You've just earned 10 points!")
else:
    print("Wow, you've just earned 15 point!")

alien_color = 'yellow' # test for yellow ('elif')
if alien_color == 'green':
    print("You've earned 5 points!")
elif alien_color == 'yellow':
    print("You've earned 10 points!")
else:
    print("Wow, you've earned 15 points!")

alien_color = 'red' # test for red ('else')
if alien_color == 'green':
    print("You've eanred 5 points!")
elif alien_color == 'yellow':
    print("You've earned 10 points!")
else:
    print("Wow, you've earned 15 points!")

# if-elif-else for stages of life

age = 22

if age < 2:
    print("You are a baby.")
elif age >= 2 and age < 4:
    print("You are a toddler.")
elif age >= 4 and age < 13:
    print("You are a kid.")
elif age >= 13 and age < 20:
    print("You are a teenager.")
elif age >= 20 and age < 65:
   print("You are an adult.")
elif age >= 65:
   print("You are a senior citizen. God bless you!")

# mutiple if statements

favorite_fruit = ['mangos', 'peaches', 'grapes', 'bananas', 'blueberries']

if 'mangos' in favorite_fruit:
    print(f"\nI sure do love {favorite_fruit[0].title()}")
if 'grapes' in favorite_fruit:
    print(f"\nI love eating grapes with cashews!")
if 'oranges' in favorite_fruit:
    print("\nDo you really like oranges like that?")
if 'peaches' in favorite_fruit:
    print("\nPeaches are unique in taste and texture. Among my favorite!")
if 'bananas' in favorite_fruit:
    print("\nI only like fresh bananas...not ripe ones.")