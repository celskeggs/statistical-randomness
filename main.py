import curses
import textwrap

SIDEPANEL_WIDTH = 40
CONSOLE_WIDTH = 100
INPUT_HEIGHT = 4
MAIN_HEIGHT = 50
FULL_HEIGHT = 1 + MAIN_HEIGHT + 1
FULL_WIDTH = 1 + SIDEPANEL_WIDTH + 1 + CONSOLE_WIDTH + 1

displayed = ["A line #%d" % i for i in range(10)]
currently_typed = ""
all_options = ["beta", "gamma", "delta", "alpha"]


def main(stdscr):
    global lines, currently_typed, displayed
    assert curses.LINES >= FULL_HEIGHT and curses.COLS >= FULL_WIDTH

    offset_y, offset_x = (curses.LINES - FULL_HEIGHT) // 2, (curses.COLS - FULL_WIDTH) // 2

    readout = curses.newwin(MAIN_HEIGHT - INPUT_HEIGHT, CONSOLE_WIDTH, offset_y + 1, offset_x + 1)
    readin = curses.newwin(INPUT_HEIGHT, CONSOLE_WIDTH, offset_y + 1 + MAIN_HEIGHT - INPUT_HEIGHT, offset_x + 1)
    sidepanel = curses.newwin(MAIN_HEIGHT, SIDEPANEL_WIDTH, offset_y + 1, offset_x + 1 + CONSOLE_WIDTH + 1)

    stdscr.addstr(offset_y, offset_x, "=" * FULL_WIDTH)
    stdscr.addstr(offset_y + FULL_HEIGHT - 1, offset_x, "=" * FULL_WIDTH)
    for y in range(offset_y + 1, offset_y + FULL_HEIGHT - 1):
        stdscr.addch(y, offset_x, "|")
        stdscr.addch(y, offset_x + CONSOLE_WIDTH + 1, "|")
        stdscr.addch(y, offset_x + CONSOLE_WIDTH + 1 + SIDEPANEL_WIDTH + 1, "|")
    stdscr.refresh()

    while True:
        readout.clear()
        for i, line in enumerate(displayed):
            readout.addstr(i, 0, line)
        readout.refresh()
        readin.clear()
        if currently_typed:
            best_options = [option for option in all_options if option.lower().startswith(currently_typed.lower())]
            relevant_options = [option for option in all_options if
                                currently_typed.lower() in option.lower() and option not in best_options]
            disp_options = best_options + [None] + relevant_options
            if disp_options[0] is None:
                disp_options = disp_options[1:]
            elif disp_options[-1] is None:
                disp_options = disp_options[:-1]
            if disp_options:
                main_option = disp_options[0]
                disp_options = [">%s<" % main_option] + disp_options[1:]
            else:
                main_option = None
        else:
            disp_options = all_options
            main_option = None

        wrapped_option_lines = textwrap.wrap(" ".join(('|' if x is None else x) for x in disp_options), CONSOLE_WIDTH)

        for i, line in enumerate((wrapped_option_lines + ["", "", ""])[:3]):
            readin.addstr(i, 0, line)
        readin.addstr(INPUT_HEIGHT - 1, 0,
                      "[%2d/%2d] ==> %s" % (len(disp_options) - disp_options.count(None), len(all_options), currently_typed))
        key = readin.getkey()
        if key == "\x1b":
            break
        elif key == "\x7f":
            currently_typed = currently_typed[:-1]
        elif key.isprintable():
            currently_typed += key
        elif key == "\n" and main_option:
            displayed.append("You selected: " + main_option)
            currently_typed = ""


stdscr = curses.initscr()
curses.noecho()
try:
    main(stdscr)
finally:
    curses.echo()
    curses.endwin()
