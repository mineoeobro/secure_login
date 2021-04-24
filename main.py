import hashlib
import json
import os.path

user_list = {}


def save_to_file(file_to_be_saved):
    file_to_json = json.dumps(file_to_be_saved)

    login_file = open("loginFile.json", "w")
    login_file.write(file_to_json)
    login_file.close()


def load_from_file():
    global user_list
    if os.path.isfile('loginFile.json'):
        user_list = json.load(open('loginFile.json'))
    else:
        user_list = {}


def check_value_type(value_to_be_checked):
    if type(value_to_be_checked) == int:
        return "int"
    elif type(value_to_be_checked) == str:
        return "str"
    else:
        return "unknown"


def value_to_hash(value_to_be_hashed):
    return hashlib.md5(value_to_be_hashed)


def good_password_check(password):
    special_character_list = ["@", "%", "+", "\\", "/", "'", "!", "#", "$", "^", "?", ":", ",", "(", ")",
                              "{", "}", "[", "]", "~", "-", "_", "."]
    if len(password) >= 8:
        for char in password:
            if char in special_character_list:
                return True
        print("Password does not have any special characters...")
        return False
    else:
        print("Password is too short, needs to be at least 8 characters long...")
        return False


def login():
    print("Login has not yet been implemented...")


def signup():
    username = input("Please enter a username: ")

    #   CHECK IF USER ALREADY IN LIST
    if username in user_list:
        print("Sorry, " + username + " has been taken...")
        signup()

    elif username not in user_list or not user_list:
        #   PASSWORD CREATION
        password = input("Please enter a password: ")
        if good_password_check(password):
            hash_pass = str(value_to_hash(password.encode("utf-8")))
            #   APPEND USERNAME AND PASSWORD TO LIST AS HASH VALUES
            user_list[username] = hash_pass
        else:
            signup()

    save_to_file(user_list)


def choose_login_type():
    login_choice = input("Would you like to login [A] or sign up [B]: ")
    if check_value_type(login_choice) == "str":
        if login_choice.lower() == "a":
            login()
        elif login_choice.lower() == "b":
            signup()
        else:
            print("That was not one of the options...")
            choose_login_type()
    else:
        print("Datatype was not a string...")


load_from_file()
print(user_list)
choose_login_type()

