import curses
from curses import wrapper

import random

import time

def main(stdscr):
    
    with open('exercises.txt','r') as file:
        exercises = [file.readline().strip() for _ in range(10)]

    random.shuffle(exercises)

    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLACK)
    
    stdscr.clear()

    # setup loop
    for i in range(0,9):

        # list exercises
        stdscr.addstr(2+(i*2),2,exercises[i])

        # exercise bar
        for j in range(0,14):
            stdscr.addstr(2+(i*2),20+j,'=',curses.color_pair(2))
        stdscr.addstr(2+(i*2),34,'O')

        # rest bar
        for j in range(0,29):
            stdscr.addstr(2+(i*2),38+j,'=',curses.color_pair(1))

        stdscr.addstr(2+(i*2),67,'O')

    stdscr.refresh()
    stdscr.getch()

    # workout loop
    for i in range(0,9):

        # highlight current exercise
        stdscr.addstr(2+(i*2),2,exercises[i],curses.color_pair(3))
        if i>0:
            stdscr.addstr(2+((i-1)*2),2,exercises[(i-1)],curses.color_pair(4))
        stdscr.refresh()

        time.sleep(2)

    stdscr.getch()

wrapper(main)