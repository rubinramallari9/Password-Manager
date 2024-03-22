import json
from tkinter import messagebox

USERNAME_KEYWORD = "username"
EMAIL_KEYWORD = "email"
PASSWORD_KEYWORD = "password"
FILE_PATH = "../data/users.json"

def add_user(**kwargs):
    try:
        with open(file=FILE_PATH, mode="r") as data_file:
            dict = json.load(data_file)
    except KeyError:
        messagebox.showerror(title="Error", message="Try again")
    else:
        if kwargs[USERNAME_KEYWORD] not in dict:
            if len(kwargs[USERNAME_KEYWORD]) != 0 or len(kwargs[EMAIL_KEYWORD]) != 0 or len(kwargs[PASSWORD_KEYWORD]) != 0:
                new_user = {
                    kwargs[USERNAME_KEYWORD]: {EMAIL_KEYWORD :kwargs[EMAIL_KEYWORD], PASSWORD_KEYWORD:kwargs[PASSWORD_KEYWORD]}
                }
                with open(file=FILE_PATH, mode="w") as data_file:
                    dict.update(new_user)
                    json.dump(dict, data_file, indent=4)
                    kwargs["function"]()
            else:
                messagebox.showerror(title="Error", message="Make sure to not let any slots empty")
        else:
            messagebox.showerror(message="User already exist. Try forgeting password", title="Error")