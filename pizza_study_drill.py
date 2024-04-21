my_pizzas = ['white sauce', 'plain cheese', 'new york']
print("These are my favorite kinds of za:")
print(my_pizzas)
friends_pizza = my_pizzas[:]
print("\nThese are my friend's favorite za:")
print(friends_pizza, "\n")

my_pizzas.append('mushroom')
friends_pizza.append('spinach')

print("Here's my appended list for pizza:")
for za in my_pizzas[:4]:
    print("\n", za.title())

print("\nHere is my friend's appended list:")
for zza in friends_pizza[:4]:
    print("\n", zza.title())

for za in my_pizzas[:3]:
    print(f"\nI really love {za.title()}...it's one of favorite kinds!")
print("\nI am pretty sure of it!")

for zza in friends_pizza:
    print(f"\nMy friend really loves {zza.title()}!")
print("\nThe only exception is: ", friends_pizza[3].title(), "...which I am impartial too.")