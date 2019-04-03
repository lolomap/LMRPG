from player import *
from os import system
from EXTRA_FILES.cheat_codes import ch_input

room = Map()
pl = Player(room)

pl.show_hud()
room.move_possibilities(pl.x, pl.y)

is_exit = False

while True:
    dir_choice = ""
    while dir_choice != "LEFT" and dir_choice != "RIGHT" and dir_choice != "FORWARD" and dir_choice != "BACK":
        dir_choice = ch_input(pl)
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

    if is_exit == -1:
        break

    if is_exit:
        room = Map()
        pl.reposition(room)
        pl.show_hud()
        room.move_possibilities(pl.x, pl.y)
