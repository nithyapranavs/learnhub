import curses
import time
from curses import wrapper
from curses.textpad import Textbox, rectangle

def main(stdscr):
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_RED)
    rb = curses.color_pair(1)
    br = curses.color_pair(2)

    win = curses.newwin(3, 18, 2, 2)
    box = Textbox(win)

    rectangle(stdscr, 1, 1, 5, 20)
    stdscr.refresh()
    box.edit()
    txt = box.gather().strip().replace("\n","")
    stdscr.addstr(10, 40, txt)
    stdscr.getch()


wrapper(main)