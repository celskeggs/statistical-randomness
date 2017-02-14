import curses

stdscr = curses.initscr()
try:
    stdscr.addstr(5, 10, "STATS " * 4)
    stdscr.refresh()
    stdscr.getkey()
finally:
    curses.endwin()
