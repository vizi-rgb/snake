import pygame as pg
import objects as s

pg.init()

# CONSTANTS
WIDTH = HEIGHT = 420

# WINDOW ATTRIBUTES
WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("WĄŻ")


def make_grid():
	pg.draw.rect(WIN,(255,0,0), (0,0,WIDTH,WIDTH), 20)

def border_touch(obj):
	if obj.head_x <= 10 or obj.head_x >= 410 or obj.head_y <= 10 or obj.head_y >= 410:
		return False 
	return True





def main():
	# LEMON
	visible_fruits_L = []
	hidden_fruits_L = []
	# APPLE
	visible_fruits_A = []
	hidden_fruits_A = []
	# WATERMELON
	visible_fruits_W = []
	hidden_fruits_W = []

	snake = s.Snake()
	run = True
	clock = pg.time.Clock()


	nametag = {0: [visible_fruits_A,hidden_fruits_A],
	 		   1: [visible_fruits_L, hidden_fruits_L],
	 		   2: [visible_fruits_W, hidden_fruits_W]}

	while run:


		clock.tick(100)

		make_grid()

		for event in pg.event.get():

			if event.type == pg.QUIT:
				run = False
				pg.quit()

		key_input = pg.key.get_pressed() 
		snake.update_vel(key_input)


		#IF THE SNAKE IS MOVING
		if snake.start():
			# AMOUNT OF SPECIFIED FRUIT TYPE TO BE HANDLED
			if len(visible_fruits_L) + len(hidden_fruits_L) < 4:
				s.Lemon(snake, visible_fruits_L)
			if len(visible_fruits_A) + len(hidden_fruits_A) < 2:
				s.Apple(snake, visible_fruits_A)
			if len(visible_fruits_W) + len(hidden_fruits_W) < 1:
				s.Watermelon(snake, visible_fruits_W)


			# VISIBLE FRUITS: RENDER, CHECK FOR COLLISIONS AND CONTROL IDLE TIME
			for i in range(3):
				for fruit in list(nametag[i])[0]:
					fruit.draw_fruit(list(nametag[i])[0], snake)
					fruit.on_collision(snake, list(nametag[i])[0], list(nametag[i])[1])
					fruit.idle_handler(list(nametag[i])[0], list(nametag[i])[1] )


			# CONTROL WHETHER A FRUIT CAN BE REMOVED TO BE THEN SPAWNED AGAIN {HIDDEN_FRUITS}
			for i in range(3): 
				# FOR FRUIT IN HIDDEN_FRUITS_A OR L OR W
				for fruit in list(nametag[i])[1]: 
					fruit.cooldown()

					if fruit.remove_ready:
						list(nametag[i])[1].remove(fruit)

			# RUN BASED ON TOUCHING THE BARRIER AND EATING ITSELF

			run = border_touch(snake) and  not snake.game_over()

		snake.cooldown() 
		snake.draw_snake()



		pg.display.update()

 # ~~~~~~ # ~~~~~~ # ~~~~~~ # ~~~~~~ # ~~~~~~ #	


WIN.fill((0,255,0))
main()				


