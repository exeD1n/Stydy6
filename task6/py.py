import json


def bank():
    login = input("Введите свой логин: ")
    password = input("Введите свой пароль: ")
    
    json_file = open ('exaple.json', 'r')
    
    a = json.load(json_file)
    
    for line in a:
        if login == line["login"] and password == line["password"]:
            print(line["id"])
    
if __name__ == "__main__":
    bank()