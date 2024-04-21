bestpals = ['duke', 'tiz', 'marv', 'q', 'bob', 'marcus', 'manny', 'eddie']
#print(bestpals[0].title())
#print(bestpals[1].title())
#print(bestpals[2].title())
#print(bestpals[3].title())
#print(bestpals[4].title())
#print(bestpals[-1].title())
#print(bestpals[-2].title())
#print(bestpals[-3].title())

# message to about my friends that includes the special {} sequence as placeholder to use 'format' method when I print
message = "I wouldn't have gotten through Oakwood without my dawg {}."

# using the 'format' method with the message variable to insert whichever 'pal' I want to fill in the placeholder. 
# also added a 'title' method for better presentation when printing
# in this case, with proper counting, I used only one negative integer just to switch things up a little, while maintaining proper syntax

#print(message.format(bestpals[0].title()))
#print(message.format(bestpals[1].title()))
#print(message.format(bestpals[2].title()))
#print(message.format(bestpals[3].title()))
#print(message.format(bestpals[4].title()))
#print(message.format(bestpals[7].title()))
#print(message.format(bestpals[-2].title()))
#print(message.format(bestpals[5].title()))

# creating a list of sudans followed to later practice modifying, adding, and removing elemnets
sudans = ['honda', 'toyota', 'nissan']
#print(sudans)

# modified the list of sudans by changing an element using the name I want followed by the index of the element I want to change, and then providing a new value
# sudans[0] = 'ford'
#print(sudans)

# using the 'append' method allowed me to add 'honda' back to the list. using 'append' will make the newly added element appear last in the list w/o affecting any of the elements in the list.
sudans.append('honda')
#print(sudans)

# build an empty list and used several 'append' calls to fill the list
sudans2 = []

sudans2.append('honda')
sudans2.append('toyota')
sudans2.append('nissan')
sudans2.append('ford')
sudans2.append('hyndai')
#print(sudans2)

# the insert method allows me to insert a new element at any position by specifying the index of the new element and the value of said new iterm
sudans.insert(2, 'hyndai')
#print(sudans)

# removing an element can be accomplished by using the 'del' method, followed by the list name and the index you want to delete
del sudans[2]
#print(sudans)

