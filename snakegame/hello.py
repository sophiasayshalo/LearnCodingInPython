import curses

def hello(stdscr):

    # get the screen size.
    sh, sw = stdscr.getmaxyx()

    msg = "Welcome to my keyboard decoding game Press ESC or q to exit!"
    stdscr.addstr(sh // 2, sw // 2 - len(msg) // 2, msg)

    while True:
        userkey = stdscr.getch()
        if userkey in [27, 113]:
            break

        msg = "ASCII CODE: {0}, Character: {1}".format(userkey, chr(userkey))
        stdscr.addstr(sh // 2 + 2, sw // 2 -len(msg) // 2, msg)       

curses.wrapper(hello)