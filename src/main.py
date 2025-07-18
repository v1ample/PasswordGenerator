import random, os, json
from help import lowercase_letters, uppercase_letters, numbers, jsondata, OpenData, UpdateData, jsonway, GetPassword, SetPassword, Clear
Clear()

password = None
allowed_characters = []

def GeneratePassword(allowed_characters):
    password_length = OpenData(jsonway, "PasswordLength")
    using_lowercase = OpenData(jsonway, "UsingLowerCase")
    using_uppercase = OpenData(jsonway, "UsingUpperCase")
    using_numbers = OpenData(jsonway, "UsingNumbers")

    allowed_characters.clear()
    password = ""

    if password_length < 1: return "Error! Your password length is too short!"
    if using_lowercase == "True": allowed_characters += lowercase_letters
    if using_uppercase == "True": allowed_characters += uppercase_letters
    if using_numbers == "True": allowed_characters += numbers

    if using_lowercase == "False" and using_uppercase == "False" and using_numbers == "False":
        return "Error! Check your settings."

    for sym in range(password_length):
        sym = random.choice(allowed_characters)
        password += str(sym)
    SetPassword(password)

def main():
    while True:
        answer = input(f"Your password: {GetPassword()}\n\n[1] Generate a password\n[2] Settings\n\nEnter: ")
        if answer == "1": 
            Clear()
            password = GeneratePassword(allowed_characters)
        elif answer == "2":
            Clear()
            setting = input(f"[1] Password length: {OpenData(jsonway, "PasswordLength")}\n[2] UsingLowerCase: {OpenData(jsonway, "UsingLowerCase")}\n[3] UsingUpperCase: {OpenData(jsonway, "UsingUpperCase")}\n[4] Using numbers: {OpenData(jsonway, "UsingNumbers")}\n[0] Back\n\nEnter: ")
            if setting == "1":
                Clear()
                while True:
                    try:
                        temp = int(input("Enter the password length\n[0] Back\n\nEnter: "))
                        if temp == 0: break; Clear(); main()
                        else: UpdateData(jsonway, "PasswordLength", temp); Clear(); main(); break
                    except ValueError: Clear()
            elif setting == "2":
                Clear()
                while True:
                    try:
                        temp1 = int(input("Should lowercase be used?\n\n[1] True\n[2] False\n[0] Back\n\nEnter: "))
                        if temp1 == 1: UpdateData(jsonway, 'UsingLowerCase', "True"); Clear(); break
                        elif temp1 == 2: UpdateData(jsonway, 'UsingLowerCase', "False"); Clear(); break
                        elif temp1 == 0: Clear(); main(); break
                    except ValueError: Clear()
            elif setting == "3":
                Clear()
                while True:
                    try:
                        temp2 = int(input("Should uppercase be used?\n\n[1] True\n[2] False\n[0] Back\n\nEnter: "))
                        if temp2 == 1: UpdateData(jsonway, 'UsingUpperCase', "True"); Clear(); break
                        elif temp2 == 2: UpdateData(jsonway, 'UsingUpperCase', "False"); Clear(); break
                        elif temp2 == 0: Clear(); main(); break
                    except ValueError: Clear()
            elif setting == "4":
                Clear()
                while True:
                    try:
                        temp3 = int(input("Should numbers be used?\n\n[1] True\n[2] False\n[0] Back\n\nEnter: "))
                        if temp3 == 1: UpdateData(jsonway, 'UsingNumbers', "True"); Clear(); break
                        elif temp3 == 2: UpdateData(jsonway, 'UsingNumbers', "False"); Clear(); break
                        elif temp3 == 0: Clear(); main(); break
                    except ValueError: Clear()
            elif setting == "0": Clear(); main()
        else: Clear()
main()
            