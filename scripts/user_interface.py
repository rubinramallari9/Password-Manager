from tkinter import *

BACKGROUND_COLOR = "#50b7ba"

class user_interface(Tk):

    def __init__(self):

        super().__init__()
        self.title("Password Manager")
        self.icon_photo = PhotoImage(file="../images/image.png")
        self.wm_iconphoto(False, self.icon_photo)
        self.config(background="#50b7ba")
        self.resizable(False, False)
        self.login_Frame()


    def login(self):
        self.email = self.emailEntry.get()
        self.password = self.passwordEntry.get()
    def register(self):

        self.register_Frame()
        self.register_frame.tkraise()
    def login_Frame(self):

        self.login_win = Frame(self, bg=BACKGROUND_COLOR)
        self.login_win.grid(row=1, column=1)
        self.login_win.tkraise()

        #Profile Picture
        canvas = Canvas(width=220, height=240, background=BACKGROUND_COLOR, highlightthickness=0)
        self.profile_picture_photo = PhotoImage(file="../images/image.png")
        self.profile_picture = canvas.create_image(110, 120, image=self.profile_picture_photo)
        canvas.grid(row=0, column=1)


        #Input

        self.emailEntry = Entry(self.login_win, width=50)
        self.emailEntry.insert(0,"Email slot")
        self.emailEntry.grid(row=1,column=1, pady=20, padx=50)


        self.passwordEntry = Entry(self.login_win, width=50)
        self.passwordEntry.insert(0,"Password slot")
        self.passwordEntry.grid(row=2,column=1, pady=20,padx=50)

        #Buttons

        login_button = Button(self.login_win, text="Log in", width=43, command=self.login)
        login_button.grid(row=3, column=1, pady=10,padx=50)

        register_button = Button(self.login_win,   text="Register", width=43, command=self.register)
        register_button.grid(row=4, column=1, pady=10,padx=50)


        forgot_password_button = Button(self.login_win,text="Forgot password", width=43, command=...)
        forgot_password_button.grid(row=5,column=1, pady=20, padx=50)

    def register_Frame(self):
        self.register_frame = Frame(self)
        self.register_frame.grid(column=1,row=1)
        self.register_frame.tkraise(self.login_win)
        # Input
        btn = Button(text="asda")
        btn.grid(row=1,column=1)
    def main_Frame(self):
        main_win = Frame(self)

    def settings_Frame(self):
        settings_win = Frame(self)