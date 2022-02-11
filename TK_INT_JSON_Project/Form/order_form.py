from tkinter import *
from tkinter import messagebox

import Controller
import glob_data
from Form import home_form
from tkcalendar import *


def renderOrder(room_data):
    print(room_data)

    # method to create new booking
    def book():
        totalDays = Controller.calculateDays(checkIn.get_date(), checkOut.get_date())
        totalCost = room_data['price'] * totalDays
        Controller.makeBook('ordersList', room_data['_id'], glob_data.current_user_data['_id'],
                            checkIn.get_date(), checkOut.get_date(), totalDays, totalCost)

        messagebox.showinfo("info", "Successful booking\n Total days: " + str(totalDays) +
                            "\n Total cost: " + str(totalCost), parent=root)
        switchHome()

    # method switch to main page
    def switchHome():
        root.destroy()
        home_form.renderMainHome()

    root = Tk()
    root.title("Hotel booking")
    root.geometry("600x700")
    heading = Label(root, text="Place order", font='Verdana 25 bold')
    heading.pack()
    # render room detail
    panel = Frame(root)
    btn_back = Button(panel, text="<< Back to Home", font='Verdana 12 bold', command=switchHome)
    btn_back.grid(row=0, column=0)
    roomPrice = Label(panel, font='Verdana 12 bold', text='Room type: ' + room_data['roomType'] +
                                                          '   Price per day: ' + str(room_data['price']))
    roomPrice.grid(row=0, column=1, padx=40)
    panel.pack(side=TOP, anchor=NW, padx=40, pady=15)
    # Add Calendar
    calendarFrame = Frame(root)
    checkInLabel = Label(calendarFrame, text="checkIn", font='Verdana 18 bold')
    checkInLabel.grid(row=0, column=0)
    checkIn = Calendar(calendarFrame, year=2021, month=8, day=5, date_pattern='mm/dd/y')
    checkIn.grid(row=1, column=0)

    checkOutLabel = Label(calendarFrame, text="CheckOut", font='Verdana 18 bold')
    checkOutLabel.grid(row=0, column=1)
    checkOut = Calendar(calendarFrame, year=2021, month=8, day=22, date_pattern='mm/dd/y')
    checkOut.grid(row=1, column=1, padx=30)

    calendarFrame.pack(pady=20)

    userInfoFrame = Frame(root)

    # Entry Box
    user_fname = StringVar()
    user_lname = StringVar()

    fname = Label(userInfoFrame, text="First name", font='Verdana 18 bold', pady=10)
    fname.grid(row=0, column=0)
    fname_entry = Entry(userInfoFrame, width=20, font='Verdana 18 bold', textvariable=user_fname)
    fname_entry.grid(row=1, column=0)
    fname_entry.insert(0, glob_data.current_user_data['fname'])

    lname = Label(userInfoFrame, text="Last name", font='Verdana 18 bold', )
    lname.grid(row=2, column=0)
    lname_entry = Entry(userInfoFrame, width=20, font='Verdana 18 bold', textvariable=user_lname)
    lname_entry.grid(row=3, column=0)
    lname_entry.insert(0, glob_data.current_user_data['lname'])

    userInfoFrame.pack(pady=30)

    btn_book = Button(root, text="Book", font='Verdana 18 bold', command=book)
    btn_book.pack()

    root.mainloop()
