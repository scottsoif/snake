import random
import curses

screen = curses.initscr()  # set the screen
curses.curs_set(0)  # removes the blinking cursor

height, width = screen.getmaxyx()
# creates new window at top of screen
window = curses.newwin(height, width, 0, 0)

window.keypad(True)
window.timeout(50) # screen refresh

snake_x = width//2
snake_y = height//2


snake = [[snake_y,snake_x],[snake_y,snake_x-1],[snake_y,snake_x-2]]
food = [height//2, width//2]

window.addch(food[0],food[1], curses.ACS_PI)

key = curses.KEY_RIGHT

while True:
	next_input = window.getch()
	key = key if next_input==-1 else next_input

	# insert key movements and end condition
	new_head = [snake[0][0], snake[0][1]]

	if key == curses.KEY_DOWN:
		new_head[0]+=1
	if key == curses.KEY_UP:
		new_head[0]-=1
	if key == curses.KEY_RIGHT:
		new_head[1]+=1
	if key == curses.KEY_LEFT:
		new_head[1]-=1

	snake.insert(0, new_head)

	# add if snake finds food

	window.addch(snake[0][0],snake[0][1], curses.ACS_CKBOARD)
	print("hi")



