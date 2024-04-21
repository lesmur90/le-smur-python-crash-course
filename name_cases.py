name = "lauren davis"
offspring_name = "lailyn"

# The method below includes an error in the string: An error message of "<built-in method upper of str object at 1030e0030>" will occur because I tried to call the 'upper' method w/o including parenthesis '()' right after it
# print(name.upper)

# Here is the correct way to call an 'upper' method. The same applies for the 'lower' and 'title' methods as well.

print(name.upper())

# testing out an f-string, while adding '.title' methods to the variables. 
# also applied are the combinations of the characters '\n', which represents a new line, and '\t' which represents an indent or tab

print(f"I have a strong declaration to make:\n\tI love {name.title()} with all of my heart.\n\tI love little {offspring_name.title()} as if she were a daughter.\n\tOne day soon, we will all live under one roof in MD.")

# experimenting with the value of the 'famous_name' variable to see if a hyphen before the name will be recognized even while trying to utilize the '.title()' method to affect the value
famous_name = "- michael jackson"

message = 'How old we you be if you never knew how old you were?'
short_phrase = "famous quote"

# using an "f-string" to insert strings within strings, also while utilizing the '\n' and '\t' characters. 
print(f'As the {short_phrase} goes, "{message}"\n\t{famous_name.title()}')

# having a hyphen in front of the value of variable does not create an error of any kind (so far) when applying a method like '.title'

# testing the 'removesuffix()' method by assigning it to a new variable
filename = 'python_notes.txt'
new_filename = filename.removesuffix('.txt')
print(new_filename)

# testing the '.removesuffix()' method by assigning it to the original variable
filename = 'python_notes.txt'.removesuffix('.txt')

print(filename)

# remember that with both the 'removeprefix()' and the 'removesuffix()' methods, to specify in the parenthesis exactly what you do not want visible when printing
