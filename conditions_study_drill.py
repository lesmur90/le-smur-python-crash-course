# writing ten true and false conditional tests

girlfriend = 'lauren'
print("Is girlfriend == 'cha'? I absolutley predict False!")
print(girlfriend == 'cha')
print("\nIs girlfriend == 'lauren'? I predict True.")
print(girlfriend == 'lauren')

my_car = 'lexus is 250'
print("Is my_car == 'acura mdx'? I predict False.")
print(my_car == 'acura mdx')
print("\nIs my_car == 'lexus is 250'? I predict True.")
print(my_car == 'lexus is 250')

color = 'pink'
print(f"\nMy favorite color recently has been {color.title()}.")
print( color == 'pink')
print("\nSome assume that my favorit color is blue.\nIs that true?")
print(color == 'blue')

food = 'mac n cheese'
print("\nMy favorite food has always been brocoli!")
print(food == 'brocoli')
print(f"\nMy favorite food is actually {food.title()}")
print(food == 'mac n cheese')

city = 'atlanta'
print("\nWhen I was in college, some people thought I was from Philly smh.")
print(city == 'philly')
print(f"\nBut I was actually born and raised in {city.upper()}, n proudly so!")
print(city == 'atlanta')

# more conditional tests
lauren_age = 33
my_age = 34
print("\nLauren and I are 30 years old or below.")

# numerical tests for equality and inequality 

print(lauren_age <= 30) and (my_age <= 30)
print(f"\nSo Lauren is {lauren_age}?")
print(lauren_age == 33)
print(f"\nAnd Steve is {my_age}?")
print(my_age == 34)


# using a tuple, for loop, and an if statement
ages = (lauren_age, my_age)
for age in ages:
    if age == 33:
        print(f"\nCongratulations Lauren, for being {age}!")
    else:
        print(f"Congratulations Steve for being {age}!")

favorite_car = 'Acura cl 3.0'
print(f"\nMy first and favorite car was the 1999 {favorite_car.title()}.")
print(favorite_car.lower() == 'acura cl 3.0')

# equality and inequality with strings

girlfriend = 'lauren'
if girlfriend != 'cha':
    print("\nWrong woman, fool!")

# testing whether a value is in a list


friends = ['marv', 'duke', 'tiz', 'ad', 'burden', 'q', 'bob']
print("Is Jalen in the friends list?")
print('jalen' in friends)
# testing whether a value is not in a list
not_friend = 'jalen'
if not_friend not in friends:
    print(f"\nI don't really bang with that man {not_friend.title()}.")

    