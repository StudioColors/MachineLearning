#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    for i in range(6):        
        while wall_is_on_the_right() == False:
            move_right()
            if wall_is_on_the_right() == False:
                fill_cell()
        move_down()
        while wall_is_on_the_left() == False:
            move_left()
            if wall_is_on_the_left() == False:
                fill_cell()
        move_down()
    move_right()
    pass


if __name__ == '__main__':
    run_tasks()
