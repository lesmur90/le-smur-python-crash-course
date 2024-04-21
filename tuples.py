#motown_25 = ('the jackson 5', 'michael jackson')
#print(motown_25)
#print(motown_25[1].title(), "\n")
#for motown in motown_25:
#    print(motown.title())

print("This is the original menu:\n")
buffet = ('mac n cheese', 'wings', 'potato wedges', 'corn', 'okra')
for menu in buffet:
    print(menu.title())

# this won't work because tuples cannont be overwritten
# buffet[0] = 'pizza'

buffet = ('mac n cheese', 'wings', 'potato wedges', 'pizza', 'nachos')
print("\nHere is the new menu:\n")
for new_menu in buffet:
    print(new_menu.title()) 
print("\nHere is the number of items on the buffet menu: ", len(buffet))