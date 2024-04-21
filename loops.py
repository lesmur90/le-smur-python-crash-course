magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician, "\n")

# every indented line following the line 'for' loop line is considered
# >>> 'inside the loop', and each indented line is executed once for 
# >>> each value in the list.
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was agreat magic show!")