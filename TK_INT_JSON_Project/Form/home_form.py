from functools import partial
from tkinter import *

# import Module to work with mongo DB
import Module
# import global variable
import glob_data
from Form import best_seller_diagram
from Form import history_form
from Form import order_form
from PIL import ImageTk, Image


# import froms


def renderMainHome():
    roomList = Module.get_data(glob_data.coll_room_list, {})

    # method to orders page
    def switchOrder(roomData):
        root.destroy()
        order_form.renderOrder(roomData)

    # method to orders history page
    def switchHistory():
        root.destroy()
        history_form.renderHistory()

    root = Tk()
    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)
    root.title('Hotel booking')
    root.geometry('800x800')
    # root.config(bg='#F2B33D')

    image = Image.open('planet-icon.png')
    image = image.resize((100, 100), Image.ANTIALIAS)
    image1 = image.resize((250, 250), Image.ANTIALIAS)
    my_img = ImageTk.PhotoImage(image)
    my_img1 = ImageTk.PhotoImage(image1)

    name_label = Label(root, text='Niagara Falls Marriott Fallsview Hotel & Spa', font=('bold', 24), padx=10, pady=10)
    name_label.pack()

    personal_panel = Frame(root)
    photoFrame = Frame(root)

    current_name = Label(personal_panel, text="Hi, " + glob_data.current_user_data['fname'], font=('bold', 12))
    current_name.grid(row=0, column=0, padx=130)
    # button  switch to user orders history
    btn_book = Button(personal_panel, text='Your booking list', command=switchHistory,
                      font=('bold', 12), fg='black', height=2)
    btn_book.grid(row=0, column=1, padx=140)

    personal_panel.pack(pady=10)
    # render image gallery
    Label(photoFrame, text="hello world", image=my_img).grid(row=3, column=0)
    Label(photoFrame, text="hello world", image=my_img1).grid(row=3, rowspan=2, column=1, columnspan=3, pady=10)
    Label(photoFrame, text="hello world", image=my_img).grid(row=4, column=0, padx=10)
    Label(photoFrame, text="hello world", image=my_img).grid(row=5, column=0, padx=10)
    Label(photoFrame, text="hello world", image=my_img).grid(row=5, column=1, padx=10)
    Label(photoFrame, text="hello world", image=my_img).grid(row=5, column=2, padx=10)
    Label(photoFrame, text="41 \n more photos", image=my_img, font=("Arial", 16), bg="#4e4e52", fg="#fafaff",
          compound='center').grid(row=5, column=3, padx=10)
    photoFrame.pack(pady=10)

    rooms_label = Label(root, text='Available rooms', font=('bold', 18), padx=20, pady=20)
    rooms_label.pack()
    # button  to show diagram
    btn_diagrma = Button(root, font='Verdana 8 bold', text='Check popular rooms',
                         command=best_seller_diagram.renderDiagram, fg='black', height=2)
    btn_diagrma.pack()
    # render dynamic room list
    typeRoom = Frame(root)
    for index, room in enumerate(roomList['data']):
        roomsFrame = LabelFrame(typeRoom, text=room['roomType'], font='Verdana 12 bold')
        roomsFrame.grid(row=0, column=index)
        my_text = Label(roomsFrame, font='Verdana 8 bold', height=2, text='For: ' + room['description'])
        my_text.grid(row=0, column=0)
        quantity = Label(roomsFrame, font='Verdana 8 bold', text=str(room['quantity']) + ' rooms left')
        quantity.grid(row=1, column=0)
        price = Label(roomsFrame, font='Verdana 8 bold', text='Price: ' + str(room['price']))
        price.grid(row=2, column=0)
        btn_book = Button(roomsFrame, font='Verdana 8 bold', text='book', command=partial(switchOrder, room),
                          fg='black', height=2, width=7)
        btn_book.grid(row=3, column=0)

    typeRoom.pack()

    root.mainloop()
