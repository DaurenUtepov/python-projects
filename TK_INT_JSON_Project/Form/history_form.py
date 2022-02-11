from functools import partial
from tkinter import *
from tkinter import messagebox

import Module
# import global variable
import glob_data
# import froms
from Form import edit_form
from Form import home_form


def renderHistory():
    orders = Module.get_data(glob_data.coll_orders_list, {'userID': glob_data.current_user_data['_id']})

    # method to update order
    def editOrder(bookID, roomID):
        root.destroy()
        room = Module.get_data_byID(glob_data.coll_room_list, roomID)
        edit_form.renderEdit(room, bookID)

    # method to delete order
    def deleteOrder(bookID, roomID):
        Module.delete_data(glob_data.coll_orders_list, {'_id': bookID})

        room = Module.get_data_byID(glob_data.coll_room_list, roomID)
        roomQuantity = room['quantity'] + 1

        Module.update_data(glob_data.coll_room_list, {'quantity': roomQuantity}, roomID)
        messagebox.showinfo("info", "Order deleted", parent=root)
        root.destroy()
        renderHistory()

    def switchHome():
        root.destroy()
        home_form.renderMainHome()

    root = Tk()
    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)

    root.title('Book history')
    root.geometry('400x800')
    name_label = Label(root, text='My booking list', font=('bold', 24), padx=20, pady=20)
    name_label.pack()

    btn_back = Button(root, text="<< Back to Home", font='Verdana 12 bold', command=switchHome)
    btn_back.pack(pady=15)

    book_list_frame = Frame(root)
    # render current user orders
    if not orders['check']:
        no_data_label = Label(root, text='No bookings', font=('bold', 24), padx=20, pady=20)
        no_data_label.pack()
    else:
        for index, book in enumerate(orders['data']):
            my_frame = Frame(book_list_frame, borderwidth=1, relief="solid")
            my_frame.grid(row=index, column=0)
            order_date = Label(my_frame, height=2,
                               text=str(index + 1) + '.' + ' FROM ' + book['fromDate'] + ' TO ' + book['toDate'])
            order_date.grid(row=0, column=0)
            order_room_type = Label(my_frame, height=2, text=" Total days: " + str(book['totalDays']))
            order_room_type.grid(row=1, column=0, sticky=NW)
            order_days = Label(my_frame, height=2, text=" Total cost: " + str(book['totalCost']))
            order_days.grid(row=2, column=0, sticky=NW)
            edit_book = Button(my_frame, text='EDIT', command=partial(editOrder, book['_id'], book['roomID']),
                               fg='black', height=2, width=7)
            edit_book.grid(row=3, column=0, padx=10, pady=10)

            dlt_book = Button(my_frame, text='DELETE', command=partial(deleteOrder, book['_id'], book['roomID']),
                              fg='black', height=2, width=7)
            dlt_book.grid(row=3, column=1, padx=10)

        book_list_frame.pack()

    root.mainloop()
