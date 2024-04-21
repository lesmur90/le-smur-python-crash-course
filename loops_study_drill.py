zas = ['white sauce', 'cheese', 'new york style']
for za in zas:
    print(f"I really love to eat {za.title()} pizza when I can!")
print("\n")

print("Pizza is not my favorit Italian dish, but it is definitely in my top five.\n")

pets = ['dogs', 'monkeys', 'parrots']
for pet in pets:
    print(f"The one thing that I like about {pet} is that they have big personalities.")
    
print("I feel like these three pets would be the amoung the easiest to communicate with.")

friend_zas = zas[:]
print(friend_zas)

zas.append('mushroom')
friend_zas.append('spinach')

print("My favorite pizzas are:\n")
for za in zas[:-1]:
    zas.append('mushrooms')
    friend_zas.append('spinach')
    print(za.title())