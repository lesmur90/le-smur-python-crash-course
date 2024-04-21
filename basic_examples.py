# whitespace examples/tests for better understanding

print("Python")

# the character \t adds a tab in the string; an indent
print("\tPython")

# the character \n adds a new line to your string. Combined with \t, your string will now be indented on each new line
print("Languages:\n\tPython\n\tC\n\tJavaScript")

# the .rstrip() method ensures that no white space exists at the right side of a string. The same goes for .lstrip() which removes whitespace from the left side of a string, and the .strip() for both sides of string containing whitespace
favorite_language = 'python '

print(favorite_language.rstrip())

favorite_language.lstrip 

# To remove prefixes, we use the .removeprefix() method

nostarch_url = 'https://nostarch.com'

print(nostarch_url.removeprefix('https://'))

simple_url = nostarch_url.removeprefix('https://')

print(simple_url)