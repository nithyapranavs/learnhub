import curses
import time
from curses import wrapper

def main(stdscr):
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_RED)

    counter_win = curses.newwin(1, 20, 10, 10)

    for i in range(101):
        counter_win.clear()
        color = curses.color_pair(1)
        if i%2 == 0:
            color = curses.color_pair(2)
        counter_win.addstr(f"{i}",color)
        counter_win.refresh()
        time.sleep(0.1)
    stdscr.getch()

wrapper(main)