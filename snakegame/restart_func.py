import curses

def game(stdscr):

    curses.curs_set(False)

    sh, sw = stdscr.getmaxyx()

    body_ch = chr(9608)

    # paint the vertical line:
    for y in range(5, sh - 5):
        stdscr.addstr(y, sw - 5, chr(9474))
    
    # paint the moving object
    body = [sh // 2, sw // 2]
    stdscr.addstr(body[0], body[1], body_ch)

    # set nodelay mode
    stdscr.nodelay(True)
    stdscr.timeout(100)

    # control while loop 
    while True:
        
        # start the game.
        # game loop
        while True:

            key = stdscr.getch()

            # ord to find chr number
            if key in [ord('q')]:
                break

            # move the object to the right by one unit
            # erase the existing unit by painting a white space
            stdscr.addstr(body[0], body[1], ' ')
            body = [body[0], body[1] + 1]
            stdscr.addstr(body[0], body[1], body_ch)

            if body[1] == sw - 5:
                # game over
                msg = "GAME OVER"
                stdscr.addstr( sh // 2, sw // 2, msg)
                msg = "press 'r' to restart or 'q' to quit"
                stdscr.addstr(sh // 2 + 1, sw // 2, msg)
                # turn off nodelay mode
                stdscr.nodelay(False)
                # break out the game loop
                break

        rkey = stdscr.getch()
        if rkey == ord('r'):
            # restart game
            # stdscr.addstr(sh // 2 + 2, sw // 2, 'restarting')
            # reset moving object to the center of the screen.
            body = [sh // 2, sw // 2]
            # turn on the nodelay mode 
            stdscr.nodelay(True)
            stdscr.timeout(100)
            # clear the screen
            stdscr.addstr( sh // 2, sw // 2, ' ' * 15)
            stdscr.addstr( sh // 2 + 1, sw // 2, ' ' * 40)
           # stdscr.addstr( sh // 2 + 2, sw // 2, ' '* 15)
        elif rkey == ord('q'):
            break
        else:
            break

        stdscr.getch()
                
curses.wrapper(game)