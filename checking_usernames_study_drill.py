current_users = ['ben', 'jen', 'scott', 'beth', 'jeff']
#current_users2 = [item.title() for item in current_users]

#print(current_users2, "\n")

new_users = ['tim', 'mary', 'ben', 'kim', 'beth']

for new_user in new_users:
    if new_user in current_users:
        print(f"The username {new_user.title()} is already taken. "
              "Please choose another username.")
    #elif any(current_users == item.title() for item in 

    else:
        print(f"Congratulations, {new_user.title()} is available.\n")

ordinal_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# most ordinal numbers end in 'th' except '1, 2, 3'
# using a loop and if-elif-else statement to output ordinal numbers

for number in ordinal_numbers:
    if number == ordinal_numbers[0]:
        print(f"{number}st")
    elif number == ordinal_numbers[1]:
        print(f"{number}nd")
    elif number == ordinal_numbers[2]:
        print(f"{number}rd")
    else:
        print(f"{number}th")