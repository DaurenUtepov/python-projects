from datetime import datetime
from tkinter import messagebox

import Module
# import global data
import glob_data


def checkLogin(email, password):
    users = Module.get_data(glob_data.coll_users_list, {'email': email})

    if not users['check']:
        print('user not found')
        return {'check': False}
    else:
        for user in users['data']:
            print(user)
            if user['password'] == password:
                print('user found')
                return {'data': user, 'check': True}
            else:
                return {'check': False}
                print('incorrect password')


def signUP(fname, lname, email, password):
    users = Module.get_data(glob_data.coll_users_list, {'email': email})
    if users['check']:
        print('user exist')
        return False
    else:
        newUser = {'fname': fname, 'lname': lname, 'email': email, 'password': password, 'comment': ""}
        Module.insertData(glob_data.coll_users_list, newUser)
        print('user created')
        return True


def makeBook(collection_name, roomID, userID, fromDate, toDate, totalDays, totalCost):
    newOrder = {"roomID": roomID, "userID": userID, "fromDate": fromDate, "toDate": toDate, "totalDays": totalDays,
                "totalCost": totalCost}
    Module.insertData(collection_name, newOrder)

    room = Module.get_data_byID(glob_data.coll_room_list, roomID)
    roomQuantity = room['quantity'] - 1

    Module.update_data(glob_data.coll_room_list, {'quantity': roomQuantity}, roomID)

    print('order created')


def calculateDays(fromDate, toDate):
    date_format = "%m/%d/%Y"
    a = datetime.strptime(fromDate, date_format)
    b = datetime.strptime(toDate, date_format)
    delta = b - a
    totalDays = delta.days
    return totalDays
