import curses

SIDEPANEL_WIDTH = 40
CONSOLE_WIDTH = 100
MAIN_HEIGHT = 50
FULL_HEIGHT = 1 + MAIN_HEIGHT + 1
FULL_WIDTH = 1 + SIDEPANEL_WIDTH + 1 + CONSOLE_WIDTH + 1


def main(stdscr):
    assert curses.LINES >= FULL_HEIGHT and curses.COLS >= FULL_WIDTH

    offset_y, offset_x = (curses.LINES - FULL_HEIGHT) // 2, (curses.COLS - FULL_WIDTH) // 2

    console = curses.newwin(MAIN_HEIGHT, CONSOLE_WIDTH, offset_y + 1, offset_x + 1)
    sidepanel = curses.newwin(MAIN_HEIGHT, SIDEPANEL_WIDTH, offset_y + 1, offset_x + 1 + CONSOLE_WIDTH + 1)


    stdscr.addstr(offset_y, offset_x, "=" * FULL_WIDTH)
    stdscr.addstr(offset_y + FULL_HEIGHT - 1, offset_x, "=" * FULL_WIDTH)
    for y in range(offset_y + 1, offset_y + FULL_HEIGHT - 1):
        stdscr.addch(y, offset_x, "|")
        stdscr.addch(y, offset_x + CONSOLE_WIDTH + 1, "|")
        stdscr.addch(y, offset_x + CONSOLE_WIDTH + 1 + SIDEPANEL_WIDTH + 1, "|")
    stdscr.refresh()

    console.addstr(5, 10, "STATS " * 4)
    console.refresh()
    stdscr.getkey()


stdscr = curses.initscr()
try:
    main(stdscr)
finally:
    curses.endwin()
