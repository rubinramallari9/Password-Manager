from tkinter import *
from twofactor_a import send_verifcationCode
from check import check


BACKGROUND_COLOR = "#50b7ba"

class user_interface(Tk):

    def __init__(self):

        super().__init__()
        self.title("Password Manager")
        self.icon_photo = PhotoImage(file="../images/image.png")
        self.wm_iconphoto(False, self.icon_photo)
        self.config(background="#50b7ba")
        self.resizable(False, False)
        self.current_frame = self.login_Frame()


    def login(self):
        username_ = self.username.get()
        email = self.emailEntry.get()
        password = self.passwordEntry.get()
        check(username=username_, email=email, password=password, function=self.main_Frame)
    def delete(self, event):
        event.widget.delete(0, END)

    def login_Frame(self):

        login_win = Frame(self, bg=BACKGROUND_COLOR)
        login_win.grid(row=1, column=1)
        login_win.tkraise()

        #Profile Picture
        canvas = Canvas(width=220, height=240, background=BACKGROUND_COLOR, highlightthickness=0)
        self.profile_picture_photo = PhotoImage(file="../images/image.png")
        self.profile_picture = canvas.create_image(110, 120, image=self.profile_picture_photo)
        canvas.grid(row=0, column=1)


        #Input
        self.username = Entry(login_win, width=50)
        self.username.bind("<FocusIn>", func=self.delete)
        self.username.insert(0, "Username")
        self.username.grid(row=1,column=1)


        self.emailEntry = Entry(login_win, width=50)
        self.emailEntry.bind("<FocusIn>", func=self.delete)
        self.emailEntry.insert(0,"Email slot")
        self.emailEntry.grid(row=2,column=1, pady=20, padx=50)

        self.passwordEntry = Entry(login_win, width=50)
        self.passwordEntry.insert(0,"Password slot")
        self.passwordEntry.grid(row=3,column=1, padx=50)
        self.passwordEntry.bind("<FocusIn>", func=self.delete)

        #Buttons

        login_button = Button(login_win, text="Log in", width=43, command=self.login)
        login_button.grid(row=4, column=1, pady=10,padx=50)

        register_button = Button(login_win,   text="Register", width=43, command=self.register_Frame)
        register_button.grid(row=5, column=1, pady=10,padx=50)


        forgot_password_button = Button(login_win,text="Forgot password", width=43, command=self.forgot_password)
        forgot_password_button.grid(row=6,column=1, pady=10, padx=50)

        return login_win

    def register_Frame(self):

        register_frame = Frame(self, background=BACKGROUND_COLOR, height=700)
        register_frame.grid(column=1,row=1)
        self.current_frame.grid_remove()
        register_frame.tkraise(register_frame)
        self.current_frame = register_frame

        # Input
        self.new_UserName = Entry(register_frame, width=50)
        self.new_Email = Entry(register_frame, width=50)
        self.new_Password = Entry(register_frame, width=50)

        self.new_UserName.insert(0, "username slot")
        self.new_Email.insert(0, "email slot")
        self.new_Password.insert(0,"password slot")

        self.new_UserName.grid(row=1,column=1,pady=10, padx=30)
        self.new_Email.grid(row=2,column=1,pady=10, padx=30)
        self.new_Password.grid(row=3, column=1, pady=10, padx=30)

        self.new_UserName.bind("<FocusIn>", func=self.delete)
        self.new_Email.bind("<FocusIn>", func=self.delete)
        self.new_Password.bind("<FocusIn>", func=self.delete)

        #Button

        confirm_button = Button(register_frame ,text="Confirm", width=43, command=...)
        confirm_button.grid(row=4, column=1, pady = 10, padx=30)


    def main_Frame(self):
        main_win = Frame(self, background=BACKGROUND_COLOR)
        self.current_frame.grid_remove()
        main_win.grid(row=1, column=1)
        self.current_frame = main_win

        #Input

        self.website_entry = Entry(main_win, width=50)
        self.email_entry = Entry(main_win, width=50)
        self.password_entry = Entry(main_win, width=27)

        self.website_entry.grid(row=1, column=1, columnspan=2, padx=20, pady=5)
        self.email_entry.grid(row=2, column=1, columnspan=2, padx= 20, pady=5)
        self.password_entry.grid(row=3, column=1, padx=20, pady=5)

        self.website_entry.bind("<FocusIn>", func=self.delete)
        self.email_entry.bind("<FocusIn>", func=self.delete)
        self.password_entry.bind("<FocusIn>", func=self.delete)



        #Buttons
        save_Button = Button(main_win, text="Generate Password", width=13)
        save_Button.grid(row=3, column=2, padx=20 ,pady=5)

        cofirm_Button = Button(main_win, text="Save", width = 43)
        cofirm_Button.grid(row=4, column=1, padx = 20, pady=10, columnspan =2)

    def forgot_password(self):
        forgotPassword_frame = Frame(self, background=BACKGROUND_COLOR)
        self.current_frame.grid_remove()
        forgotPassword_frame.grid(row=1, column=1)
        self.current_frame = forgotPassword_frame


        self.user_email_F = Entry(forgotPassword_frame,   width=50)
        self.user_email_F.insert(0,"Email Slot")
        self.user_email_F.grid(row=1, column=1, padx = 20 , pady=10)
        self.user_email_F.bind("<FocusIn>", func=self.delete)

        self.btn_send_2FA = Button(forgotPassword_frame,text="Send Code",width=43 , command=self.confirmation)
        self.btn_send_2FA.grid(row=2, column=1, padx= 20,pady=10, columnspan=2)

    def confirmation(self):
        self.btn_send_2FA.grid_remove()
        self.user_email_F.grid_remove()
        self.twoFA_code = Entry(self.current_frame, width=50)
        self.twoFA_code.insert(0,"Code Slot")
        self.twoFA_code.bind("<FocusIn>", func=self.delete)
        self.twoFA_code.grid(row=1,column=1, padx=20, pady=10)
        self.btn_Confirm = Button(text="Confirm", width=43, command=...)
        self.btn_Confirm.grid(row=2, column=1, padx=20, pady=10)
    def settings_Frame(self):
        settings_win = Frame(self)
