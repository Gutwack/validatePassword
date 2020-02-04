#cap = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#sym = ['?', '!']

import re

password = input("Please enter a new password (5 letters min): ")
x = True

while x:
    if (len(password) < 5):
        break
    elif not re.search("[A-Z]", password):
        print("Password missing uppercase letter")
        x = False
        continue
    elif not re.search("[0-9]", password):
        print("Password missing number")
        x = False
        continue
    elif not re.search("[?!]", password):
        print("Password missing '?' or '!'")
        x = False
        continue
    else:
        x = False
        print("New password set")
        break

        
