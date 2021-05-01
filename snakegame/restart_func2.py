import curses

def setup_game(stdscr, sh, sw, ch):

    stdscr.addstr(3, 50, "Welcome to my mini Game!")

    # paint the vertical line:
    for y in range(5, sh - 5):
        stdscr.addstr(y, sw - 5, chr(9474))
    
    # paint the moving object
    body = [sh // 2, sw // 2 + 10]
    stdscr.addstr(body[0], body[1], ch)

    # set nodelay mode 
    stdscr.nodelay(True)
    stdscr.timeout(100)

    return body

def game(stdscr):

    # turn off cursor.
    curses.curs_set(False)

    sh, sw = stdscr.getmaxyx()

    body_ch = chr(9608)
    body = setup_game(stdscr, sh, sw, body_ch)

    # controle while loop
    while True:
        # start the game.
        # game loop
        while True:
            key = stdscr.getch()
    
            #if key in [ord('q')]:
            #    break
    
            # move the object to right by one unit:
            # erase the existing unit by paint a white space,
            stdscr.addstr(body[0], body[1], ' ')
            body = [body[0], body[1] + 1]
            stdscr.addstr(body[0], body[1], body_ch)
    
            if body[1] == sw - 5:
                # game over 
                msg = "GAME OVER."
                stdscr.addstr( sh // 2, sw // 2, msg)
                msg = "Press 'r' to restart game or Press 'q' to quit!"
                stdscr.addstr( sh // 2 + 1, sw // 2, msg)
                # turn off nodelay mode
                stdscr.nodelay(False)
                # break out the game loop
                break
                
        rkey = stdscr.getch()
        if rkey == ord('r'):
            # restart game...
            # clearn screen.
            stdscr.clear()
            # reset game board
            body = setup_game(stdscr, sh, sw, body_ch)
        elif rkey == ord('q'):
            break
        else:
            break

    #stdscr.getch()

curses.wrapper(game)