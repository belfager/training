import curses
from curses import wrapper

import random

import time

from playsound import playsound

def count_lines_in_file(filename):

    try:
        # Open the file in read mode ('r')
        with open(filename, 'r', encoding='utf-8') as file:
            line_count = 0
            # Iterate through each line of the file and increment the counter
            for line in file:
                line_count += 1
            return line_count
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def main(stdscr):

    l = count_lines_in_file('exercises.txt')
    
    with open('exercises.txt','r') as file:
        exercises = [file.readline().strip() for _ in range(l)]

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

        # rest bar
        for j in range(0,14):
            stdscr.addstr(2+(i*2),20+j,'—',curses.color_pair(2))    # blue
        stdscr.addstr(2+(i*2),34,'•')

        # exercise bar
        for j in range(0,29):
            stdscr.addstr(2+(i*2),38+j,'—',curses.color_pair(1))    # green

        stdscr.addstr(2+(i*2),67,'•')

    stdscr.refresh()
    stdscr.getch()

    # workout loop
    for i in range(0,9):

        # highlight current exercise
        stdscr.addstr(2+(i*2),2,exercises[i],curses.color_pair(3))
        if i>0:
            stdscr.addstr(2+((i-1)*2),2,exercises[(i-1)],curses.color_pair(4))  # white
        stdscr.refresh()

        # countdown exercise
        for j in range(29,-1,-1):
            stdscr.addstr(2+(i*2),38+j,'•',curses.color_pair(4))    # white
            stdscr.addstr(2+(i*2),39+j,' ',curses.color_pair(2))    # blue
            stdscr.refresh()

            # play sound on last three pips
            if (j<3) and (j>0):
                playsound("beep1.mp3")
            else:
                time.sleep(1)

            if j==0:
                playsound("beep2.mp3")
            else:
                time.sleep(1)

        # countdown rest
        for j in range(14,-1,-1):
            stdscr.addstr(2+(i*2),20+j,'•',curses.color_pair(4))    # white
            stdscr.addstr(2+(i*2),21+j,' ',curses.color_pair(1))    # green
            stdscr.refresh()

            # play sound on last three pips
            if (j<3) and (j>0):
                playsound("beep1.mp3")
            else:
                time.sleep(1)

            if j==0:
                playsound("beep2.mp3")
            else:
                time.sleep(1)

            time.sleep(2)

        time.sleep(2)

    stdscr.getch()

wrapper(main)