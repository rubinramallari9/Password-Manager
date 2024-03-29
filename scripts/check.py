from tkinter import messagebox
import json



def check(username, email, password, function):
    with open("../data/users.json", "r") as file:
        data = json.load(file)
    try:

        if email == data[username]["email"] and password == data[username]["password"]:
            messagebox.showinfo(title="Logged On", message="You have logged successfully")
            function()
        else:
            messagebox.showerror(title="Error", message="Try again")
    except KeyError:
        messagebox.showerror(title="Not Found", message="Check again your account details or click 'forgot password'")
