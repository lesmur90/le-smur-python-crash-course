equ1 = 2 + 3
equ2 = 3 - 2
equ3 = 2 * 3
equ4 = 3 / 2

# two muplitiplication symbols "**" represent exponents

equ5 = 3 ** 2
equ6 = 8 ** 8
equ7 = 2 + 3 * 4

print(equ6 / equ7 - equ3)

combo = equ6 / equ7 - equ3
short_phrase = "floating number"
message = f"From my understanding, number like {combo} is an example of a {short_phrase}, or simply put: 'float'. "

# placed the 'title' method in the original variable so I would not have to write it later on in the printing method
validity = "true".title()

# added a special {} sequence to serve as a place holder when a 'format' method is used.
message2 = "True or False?: {}"

#statement = message "{}"

# the format method in this case was a little tricky when I initally tried to add special {} sequence at the end of the 'message' variable. It read as an syntax error. Thus, I created 'message2' to for a smoother run/to avoid any errors
print(message + message2.format(validity))