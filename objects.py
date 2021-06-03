import pygame as pg
import random
import os

WIDTH = 420
WIN = pg.display.set_mode((WIDTH,WIDTH))

class Snake:
	def __init__(self, h_x = 210, h_y = 210, l = 1, vel = 10, t_0 = 40):
		self.head_x = h_x
		self.head_y = h_y
		self.vel_x = 0
		self.vel_y = 0
		self.vel_0 = vel
		self.level = l
		self.last_head_pos = []
		self.time_to_move = t_0
		self.cooldown_counter = 0

	def draw_snake_head(self):
		pg.draw.rect(WIN, (0,191,255) , (self.head_x,self.head_y, 10,10))
		if (self.head_x, self.head_y) not in self.last_head_pos:
			self.last_head_pos.append((self.head_x, self.head_y))

		while len(self.last_head_pos) > self.level:
			self.last_head_pos.pop(0)

	def draw_snake_body(self):
		for pos in self.last_head_pos:
			if pos != (self.head_x, self.head_y):
				pg.draw.rect(WIN, (255,255,255), (pos[0], pos[1], 10, 10))

	def draw_snake(self): 
		# Draws the snake at the time_to_move frequency
		if self.cooldown_counter == 0:
			WIN.fill((0,255,0), (10,10, WIDTH - 20, WIDTH - 20))
			self.update_pos()
			self.draw_snake_head()
			self.draw_snake_body()
		self.cooldown_counter += 1

	def update_vel(self, key_input):	   
		if key_input[pg.K_w] and abs(self.vel_y) != self.vel_0:		
			self.vel_y = - self.vel_0
			self.vel_x = 0
		elif key_input[pg.K_s] and abs(self.vel_y) != self.vel_0:
			self.vel_y = self.vel_0
			self.vel_x = 0
		elif key_input[pg.K_a]  and abs(self.vel_x) != self.vel_0:
			self.vel_x = - self.vel_0
			self.vel_y = 0
		elif key_input[pg.K_d]  and abs(self.vel_x) != self.vel_0:
			self.vel_x = self.vel_0
			self.vel_y = 0

	def update_pos(self):
		self.head_x = self.head_x + self.vel_x
		self.head_y = self.head_y + self.vel_y

	def cooldown(self):	
		if self.cooldown_counter >= self.time_to_move:
			self.cooldown_counter = 0

	def speed_handler(self):
		if self.time_to_move > 5:
			self.time_to_move -= 1


	def start(self):
		if self.vel_x == 0 and self.vel_y == 0:
			return False
		return True

	def game_over(self):
		return (self.head_x, self.head_y) in self.last_head_pos[:-1]


class Fruit:
	def __init__(self, obj, source, m, t, visible_fruits, t1):
		self.x, self.y = random.randint(1,40)*10,random.randint(1,40)*10
		while (self.x, self.y) in obj.last_head_pos or (self.x, self.y) in visible_fruits:
			self.x, self.y = random.randint(1,40)*10, random.randint(1,40)*10

		self.multiplier = m

		self.time_to_spawn = t
		self.time_to_spawn_counter = 0 

		self.idle_time = t1
		self.idle_time_counter = 0

		self.img = pg.image.load(os.path.join("assets", source))
		self.collision_count = 0

		self.fade_counter = 0

		self.remove_ready = False
		visible_fruits.append(self)

	def on_collision(self, obj, visible_fruits, hidden_fruits):
		if ((obj.head_x, obj.head_y) == (self.x, self.y) and
			self.collision_count == 0):

			obj.level += self.multiplier
			obj.speed_handler()
			visible_fruits.remove(self)
			hidden_fruits.append(self)
			self.time_to_spawn_counter += 1 
			self.collision_count += 1
		elif ((obj.head_x, obj.head_y) == (self.x, self.y) and
			self.collision_count > 0):

			self.collision_count += 1

	def draw_fruit(self, visible_fruits, obj):
		if self.fade_handler():
			self.fade_counter += 1
			if self.fade_counter == obj.time_to_move * 2:
				self.fade_counter = 0
				WIN.blit(self.img, (self.x, self.y))
			
		else:
			WIN.blit(self.img,(self.x, self.y))	



	def cooldown(self):
		if self.time_to_spawn <= self.time_to_spawn_counter:
			self.time_to_spawn_counter = 0
			self.remove_ready = True
		elif self.time_to_spawn_counter > 0:
			self.time_to_spawn_counter += 1


	def idle_handler(self,visible_fruits, hidden_fruits):

		self.idle_time_counter += 1

		if self.idle_time_counter >= self.idle_time:
			visible_fruits.remove(self)
			hidden_fruits.append(self)
			self.time_to_spawn_counter += 1 

	def fade_handler(self):
		if self.idle_time_counter >= (0.75 * self.idle_time):
			return True
		else:
			return False


class Lemon(Fruit):
	def __init__(self, obj, visible_fruits):
		super().__init__(obj, "lemon.png", 1, 300, visible_fruits, 2000)

class Apple(Fruit):
	def __init__(self, obj, visible_fruits):
		super().__init__(obj, "apple.png", 2, 400, visible_fruits, 1500)

class Watermelon(Fruit):
	def __init__(self, obj, visible_fruits):
		super().__init__(obj, "watermelon.png", 3, 500, visible_fruits, 1000)




