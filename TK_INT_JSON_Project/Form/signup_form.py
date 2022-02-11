from tkinter import *
from tkinter import messagebox

# import controllers
import Controller
# import forms
from Form import login_form


# import global data


def renderSignUP():
    # method to switch login page
    def close():
        root.destroy()
        login_form.renderLogin()

    # method to check if new user exist if not create new user
    def btn_signUp():
        if first_name.get() == "" or last_name.get() == "" or user_email.get() == "" or password.get() == "":
            messagebox.showinfo("info", "Please fill all the fields", parent=root)
        else:
            check = Controller.signUP(first_name.get(), last_name.get(), user_email.get(), password.get())
            if check:
                messagebox.showinfo("info", "User created", parent=root)
                close()
            else:
                messagebox.showinfo("info", "user with given email exist", parent=root)

    root = Tk()
    root.title("Hotel booking signup")
    root.geometry("500x500")

    # heading label
    heading = Label(root, text="Signup", font='Verdana 20 bold')
    heading.place(x=80, y=60)

    # form data label
    first_name_label = Label(root, text="First Name :", font='Verdana 10 bold')
    first_name_label.place(x=80, y=130)

    last_name_label = Label(root, text="Last Name :", font='Verdana 10 bold')
    last_name_label.place(x=80, y=160)

    email_label = Label(root, text="Email :", font='Verdana 10 bold')
    email_label.place(x=80, y=190)

    password_label = Label(root, text="Password :", font='Verdana 10 bold')
    password_label.place(x=80, y=220)

    # Entry Box

    first_name = StringVar()
    last_name = StringVar()
    user_email = StringVar()
    password = StringVar()

    first_name_entry = Entry(root, width=40, textvariable=first_name)
    first_name_entry.place(x=200, y=133)

    last_name_entry = Entry(root, width=40, textvariable=last_name)
    last_name_entry.place(x=200, y=163)

    user_email_entry = Entry(root, width=40, textvariable=user_email)
    user_email_entry.place(x=200, y=190)

    password_entry = Entry(root, width=40, show="*", textvariable=password)
    password_entry.place(x=200, y=220)

    # button signup
    btn_signup = Button(root, text="Sign Up", font='Verdana 10 bold', command=btn_signUp)
    btn_signup.place(x=200, y=260)

    root.mainloop()
