import curses

def colors(stdscr):

    curses.start_color()
    curses.use_default_colors()
    
    stdscr.addstr(1, 0, "")
    for i in range(0, curses.COLORS):
        # initialize the colour pair
        curses.init_pair(i + 1, i, -1)
        stdscr.addstr("[{0}]".format (str(i + 1)), curses.color_pair(i + 1))

    stdscr.getch()
    
curses.wrapper(colors)