cars = ['audi', 'bmw', 'subaru', 'toyota']

# using an 'if statement' w/in a 'for loop' to sift the list of cars 
# for 'bmw'. if it finds 'bmw', print it in uppercase letters
# else, print the list as regular proper noun w/'title()' method
for car in cars:
    if car =='bmw':
        print(car.upper())
    else:
        print(car.title())\

# when checking for inequality, use the inequality operator: '!='
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("\nHold the anchovies!")