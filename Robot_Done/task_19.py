#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_29():
    while wall_is_on_the_right() == False and wall_is_above() == True:
        move_right()
    while wall_is_on_the_left() == False and wall_is_above() == True:
        move_left()

    if wall_is_on_the_right() == True:
        while wall_is_above() == False:
            move_up()
        while wall_is_on_the_left() == False:
            move_left()

    else:
        while wall_is_above() == False:
            move_up()

    if (wall_is_on_the_left() and wall_is_above() and wall_is_beneath()) == True:
        move_right(8)
    pass


if __name__ == '__main__':
    run_tasks()
