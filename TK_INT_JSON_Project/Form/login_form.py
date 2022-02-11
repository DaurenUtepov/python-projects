from tkinter import *
from tkinter import messagebox

# import controllers
import Controller
# import global data
import glob_data
# import forms
from Form import home_form
from Form import signup_form


def renderLogin():
    # method to signup page
    def switchSignup():
        root.destroy()
        signup_form.renderSignUP()

    # method to check login and password
    def btnLogin():
        if user_email.get() == "" or password.get() == "":
            messagebox.showinfo("info", "Please fill all the fields", parent=root)
        else:
            check = Controller.checkLogin(user_email.get(), password.get())
            if check['check']:
                glob_data.current_user_data = check['data']
                root.destroy()
                home_form.renderMainHome()
            else:
                messagebox.showinfo("info", "Please enter valid Email an Password", parent=root)

    root = Tk()
    root.title("Hotel booking")
    root.geometry("500x500")

    # heading label
    heading = Label(root, text="Login", font='Verdana 25 bold')
    heading.place(x=80, y=150)

    username = Label(root, text="User email :", font='Verdana 10 bold')
    username.place(x=80, y=220)

    userpass = Label(root, text="Password :", font='Verdana 10 bold')
    userpass.place(x=80, y=260)

    # Entry Box
    user_email = StringVar()
    password = StringVar()

    userentry = Entry(root, width=40, textvariable=user_email)
    userentry.place(x=200, y=223)

    passentry = Entry(root, width=40, show="*", textvariable=password)
    passentry.place(x=200, y=260)

    # button login and Sign Up

    btn_login = Button(root, text="LogIn", font='Verdana 10 bold', command=btnLogin)
    btn_login.place(x=200, y=293)

    btn_signup = Button(root, text="SignUp", font='Verdana 10 bold', command=switchSignup)
    btn_signup.place(x=280, y=293)

    root.mainloop()
