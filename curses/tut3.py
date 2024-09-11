import curses
import time
from curses import wrapper

def main(stdscr):
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_RED)

    pad = curses.newpad(100, 100)
    stdscr.refresh()

    for i in range(100):
        for j in range(26):
            char = chr(65+j)
            pad.addnstr(char, curses.color_pair(2))
    for i in range(50):
        stdscr.clear()
        stdscr.refresh()
        pad.refresh(0, i, 5, i, 15, 25 + i)
        time.sleep(0.1)
    stdscr.getch()

wrapper(main)