import pygame as pg
import objects as s

pg.init()

# CONSTANTS
WIDTH = HEIGHT = 420
#

WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("WĄŻ")

def make_grid():
	WIN.fill((0,255,0))
	pg.draw.rect(WIN,(255,0,0), (0,0,WIDTH,WIDTH), 20)

def border_touch(obj):
	if obj.head_x <= 10 or obj.head_x >= 410 or obj.head_y <= 10 or obj.head_y >= 410:
		return False 
	return True




def main():
	visible_fruits = []
	hidden_fruits = []
	snake = s.Snake()
	run = True
	clock = pg.time.Clock()

	while run:

		clock.tick(100)

		for event in pg.event.get():

			if event.type == pg.QUIT:
				run = False
				pg.quit()

		key_input = pg.key.get_pressed() 
		snake.update_vel(key_input)

		snake.cooldown() 
		snake.draw_snake()

		if snake.start():
			if len(visible_fruits) + len(hidden_fruits) < 4:
				s.Lemon(snake, visible_fruits)

			for fruit in visible_fruits:
				fruit.draw_fruit(visible_fruits) 
				fruit.on_collision(snake, visible_fruits, hidden_fruits)
				fruit.idle_handler(visible_fruits, hidden_fruits)
			for fruit in hidden_fruits:
				fruit.cooldown()
				if fruit.remove_ready:
					hidden_fruits.remove(fruit)
			run = border_touch(snake) and  not snake.game_over()
		pg.display.update()

 # ~~~~~~ # ~~~~~~ # ~~~~~~ # ~~~~~~ # ~~~~~~ #	


make_grid()	
main()				


