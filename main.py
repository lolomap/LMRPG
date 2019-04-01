from player import *
from os import *

room = Map()
pl = Player(room)

room.show_map()
print(pl.x, pl.y)

pl.show_hud()
room.move_possibilities(pl.x, pl.y)

is_exit = False

while True:
    dir_choice = ""
    while dir_choice != "LEFT" and dir_choice != "RIGHT" and dir_choice != "FORWARD" and dir_choice != "BACK":
        dir_choice = input()
        dir_choice = dir_choice.upper()
    system("cls")
    pl.show_hud()

    if dir_choice == "LEFT" and room.is_left:
        is_exit = pl.move(room, -1, 0)
    elif dir_choice == "RIGHT" and room.is_right:
        is_exit = pl.move(room, 1, 0)
    elif dir_choice == "FORWARD" and room.is_forward:
        is_exit = pl.move(room, 0, -1)
    elif dir_choice == "BACK" and room.is_back:
        is_exit = pl.move(room, 0, 1)

    if is_exit:
        room = Map()
        pl.reposition(room)
        pl.show_hud()
        room.move_possibilities(pl.x, pl.y)
