from collections import Counter

import Module
import glob_data
import matplotlib.pyplot as plt
import numpy as np


def renderDiagram():
    booked_rooms = Module.get_data(glob_data.coll_orders_list, {})
    room_list = Module.get_data(glob_data.coll_room_list, {})

    rooms_name = []
    booking_quantity = []
    for x in booked_rooms['data']:
        booking_quantity.append(x['roomID'])

    for j in room_list['data']:
        for h in booking_quantity:
            if j['_id'] == h:
                rooms_name.append(j['roomType'])
    c = Counter(rooms_name)
    print(c)

    array1 = []
    array2 = []
    for x, y in c.items():
        array1.append(x)
        array2.append(y)

    x = np.array(array1)
    y = np.array(array2)

    plt.bar(x, y)
    plt.title("Popular room types")
    plt.xlabel("Rooms type")
    plt.ylabel("Room quantity")
    plt.show()
