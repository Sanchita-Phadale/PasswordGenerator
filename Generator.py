import string
import random
import secrets

# Getting password length
length = int(input("Enter password length: "))

print('''Choose character set for password from these :
1. Letters
2. Digits
3. Special characters
4. Alphanumeric
5. Exit''')

characterList = ""

# Getting character set for password
while(True):
    
    choice = int(input("Pick a number "))
    if(choice == 1):
        # Adding letters to possible characters
        characterList += string.ascii_letters
        break
    elif(choice == 2):
        # Adding digits to possible characters
        characterList += string.digits
        break
    elif(choice == 3):
        # Adding special characters to possible
        # characters
        characterList += string.punctuation
        break
    elif(choice == 4):
        letters = string.ascii_letters
        digits = string.digits
        special_chars = string.punctuation
        characterList = letters + digits + special_chars
        break
    elif(choice==5):
        break
    else:
        print("Please pick a valid option!")

if len(characterList)>0:
    for i in range(length):
        
        #password += ''.join(random.choice(characterList))
        password += ''.join(secrets.choice(characterList))

    # printing password as a string
    print("The random password is " + "".join(password))
else:
    print("Good Bye")
