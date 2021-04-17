import curses
from curses import textpad
import random

def paint_score(stdscr, score):

    sh, sw = stdscr.getmaxyx()
    # paint score:
    stdscr.addstr(3, sw // 4, 'SCORE: ')
    stdscr.addstr(str(score))
    

def board(stdscr):

    # turn off cursor
    curses.curs_set(False)
    # turn around without delay
    stdscr.nodelay(1)
    # timeout in million second
    stdscr.timeout(170)

    # screen size
    sh, sw = stdscr.getmaxyx()
    # set x, y to center of screen
    center = [sh // 2, sw // 2]

    # set welcome message
    welcome_msg = 'SNAKE GAME'
    stdscr.addstr(1, center[1]- len(welcome_msg) // 2, welcome_msg)
    welcome_msg = 'PRESS THE ARROW KEYS TO CHANGE DIRECTION. PRESS ESC TO EXIT.'
    stdscr.addstr(2, center[1] - len(welcome_msg) // 2, welcome_msg)


    # define the gameboard
    box = [
    [4, 3],
    [sh - 3, sw - 3]  
    ]

    # draw the border of the gameboard
    textpad.rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1])

    # define snake body
    snake = [
        # head 
        [center[0], center[1] + 1],
        # body 
        [center[0], center[1]],
        # tail
        [center[0], center[1] - 1]
    ]
    
    # █ 9608
    snake_ch = chr(9608)

    # draw snake body
    for point in snake:
        stdscr.addstr(point[0], point[1], snake_ch)


    # set direction of snake
    direction = curses.KEY_RIGHT

    # variable for food's location
    food_ch = "*"
    food = [
        random.randint(box[0][0] + 1, box[1][0] - 1),
        random.randint(box[0][1] + 1, box[1][1] - 1)
    ]
    # paint food
    stdscr.addstr(food[0], food[1], food_ch)

    score = 0
    paint_score(stdscr, score)
    score_step = 5

    while True:
        key = stdscr.getch()
        # ESC key 
        if key == 27:
            break

        # snake's moving direction based on input
        if key == curses.KEY_UP:
            direction = key
        elif key == curses.KEY_LEFT:
            direction = key
        elif key == curses.KEY_RIGHT:
            direction = key
        elif key == curses.KEY_DOWN:
            direction = key

        # move the snake one to the right
        head = snake[0]
        # direction moved based on key pressed
        if direction == curses.KEY_UP:
            new_head = [head[0] - 1, head[1]]
        elif direction == curses.KEY_RIGHT: 
            new_head = [head[0], head[1] + 1]
        elif direction == curses.KEY_DOWN: 
            new_head = [head[0] + 1, head[1]]
        elif direction == curses.KEY_LEFT:
            new_head = [head[0], head[1] - 1]
        # paint new head 
        stdscr.addstr(new_head[0], new_head[1], snake_ch)
        # update snake variable
        snake.insert(0, new_head)

        if snake[0][0] == food[0] and snake[0][1] == food[1]:
            # increase the score
            score += score_step
            paint_score(stdscr, score)

        
            # generate new food (x axis, y axis)
            food = [
                # x axis
                random.randint(box[0][0] + 1, box[1][0] - 1),
                # y axis
                random.randint(box[0][1] + 1, box[1][1] - 1)
            ]
            # draw the food
            stdscr.addstr(food[0], food[1], food_ch)
        else: 
            # draw empty string
            stdscr.addstr(snake[-1][0], snake[-1][1], " ")
            # remove the tail
            snake.pop()

        if (snake[0][0] in [box[0][0], box[1][0]] or
            snake[0][1] in [box[0][1], box[1][1]]):

            msg = "GAME OVER."
            stdscr.addstr(center[0], center[1] - len(msg)//2, msg)
            # turn off nodelay mode
            stdscr.nodelay(0)
            stdscr.getch()
            break
   

curses.wrapper(board)