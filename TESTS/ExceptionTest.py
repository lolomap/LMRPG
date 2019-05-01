from player import *
from TESTS import LOGGER

# ***TEST PARAMS***
TEST_RUN = 1000
TEST_NAME = "ExceptionTestLogs/ExceptionTest"
TEST_COUNTER = open("ExceptionTestCount.cn", "r+")
TEST_NUMBER = TEST_COUNTER.read()
TEST_LOGGING = True
# *****************


if TEST_LOGGING:
    logger = LOGGER.Logger(TEST_NAME+TEST_NUMBER+".log")

room = Map()
pl = Player(room)

# Giving cheat params to player
ch_input(pl, "gw")
ch_input(pl, "ga")
ch_input(pl, "hl")

PASSED_TESTS_COUNT = 0
FAILED_PASSED_TESTS_COUNT = 0

is_exit = False

for i in range(TEST_RUN):
    try:
        # Current info about player and map
        pl.show_hud()
        room.show_map()
        print("x=", pl.x, "y=", pl.y)
        room.move_possibilities(pl.x, pl.y)
        DIR_VARIANTS = []
        if room.is_forward:
            DIR_VARIANTS.append("FORWARD")
        if room.is_back:
            DIR_VARIANTS.append("BACK")
        if room.is_right:
            DIR_VARIANTS.append("RIGHT")
        if room.is_left:
            DIR_VARIANTS.append("LEFT")
        dir_choice = rand.choice(DIR_VARIANTS)
        print(dir_choice)

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

    except Exception as ex:
        print("\n\n*******\nTEST FAILED")
        print(type(ex).__name__, ex.args, "\n*******\n\n")
        FAILED_PASSED_TESTS_COUNT += 1
    else:
        print("\n\n*******\nTEST PASSED\n*******\n\n")
        PASSED_TESTS_COUNT += 1

# Test results
TEST_RESULT = "\n\nPASSED TESTS: {0}\nFAILED TESTS: {1}\n\n".format(PASSED_TESTS_COUNT, FAILED_PASSED_TESTS_COUNT)
print(TEST_RESULT)

if TEST_LOGGING:
    logger.close()
    TEST_COUNTER.truncate(0)
    TEST_COUNTER.seek(0)
    TEST_COUNTER.write(str(int(TEST_NUMBER)+1))
    TEST_COUNTER.close()

# TODO: fix endless battle
