user_names = ['ben', 'kay', 'jeff', 'sue', 'admin']

for user_name in user_names:
    if user_name == 'admin':
        print(f"Hello {user_name.title()}, would you like to "
              "see a status report?\n")
    else:
        print(f"Hello {user_name.title()}, thank you for logging in again.")

user_names = []
if user_names:
    print(f"Welcome {user_names.title()}!")
else:
    print("We need to find some users!")