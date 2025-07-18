import os, time, json

jsonway = "src\\data.json"

jsondata = {
    "PasswordLength": 5,
    "UsingLowerCase": "True",
    "UsingUpperCase": "False",
    "UsingNumbers": "False"
}

lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

def Clear(seconds=0):
    time.sleep(seconds)
    os.system("cls")

def OpenData(way, setting):
    try:
        with open(way) as file:
            data = json.load(file)
            return data[setting]
    except FileNotFoundError:
        with open(way, 'x') as file:
            json.dump(jsondata, file)
            data = json.load(file)
            return data[setting]
def UpdateData(way, setting, value):
    try:
        with open(way, 'r') as file:
            data = json.load(file)
            data[setting] = value
            with open(way, 'w') as file:
                json.dump(data, file)
    except FileNotFoundError:
        with open(way, 'x') as file:
            json.dump(jsondata, file)
            data = json.load(file)
            data[setting] = value
            with open(way, 'w') as file:
                json.dump(data, file)

def SetPassword(password):
    with open("src//password.txt", 'w') as file:
        file.write(password)

def GetPassword():
    with open("src\\password.txt") as file:
        password = file.read()
        return password
