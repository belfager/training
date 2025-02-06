import curses
from curses import wrapper

import random

def main(stdscr):
    
    with open('exercises.txt','r') as file:
        exercises = [file.readline().strip() for _ in range(10)]

    random.shuffle(exercises)
    
    stdscr.clear()

    for i in range(0,9):
        stdscr.addstr(2+(i*2),2,exercises[i])

        for j in range(0,14):
            stdscr.addstr(2+(i*2),20+j,'=')

        stdscr.addstr(2+(i*2),34,'O')

        for j in range(0,29):
            stdscr.addstr(2+(i*2),38+j,'=')

        stdscr.addstr(2+(i*2),67,'O')

    stdscr.refresh()
    stdscr.getch()

wrapper(main)