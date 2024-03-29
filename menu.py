import pickle
import pygame as pg
import os 
pg.init()

WIDTH = HEIGHT = 420
WIN = pg.display.set_mode((WIDTH,HEIGHT))

class MainMenu:
	PLAY_BUTTON = pg.image.load(os.path.join("assets", "play.png"))
	DATA_BUTTON = pg.image.load(os.path.join("assets", "data.png"))
	QUIT_BUTTON = pg.image.load(os.path.join("assets", "quit.png"))

	@classmethod
	def draw_menu(cls):
		WIN.fill((134,19,159))
		WIN.blit(cls.PLAY_BUTTON, (80,80))
		WIN.blit(cls.QUIT_BUTTON, (80, 212))
		WIN.blit(cls.DATA_BUTTON, (212,212))

		for x in cls.on_play(), cls.on_quit(), cls.on_data():
			if x != False: 
				width, height = (x[2] - x[1]), (x[4] - x[3])
				tempSurface = pg.Surface((width, height))
				tempSurface.set_alpha(100)
				WIN.blit(tempSurface, (x[1], x[3]))
				if x[2] == 207: 
					pg.draw.rect(WIN, (255,0,0), (x[1],x[3], width, height), 4)
				else:
					pg.draw.rect(WIN, (0,255,0), (x[1],x[3], width, height), 4)

	@classmethod	
	def on_play(cls):
		x1,x2,y1,y2 = 80, 340, 80, 207
		if (pg.mouse.get_pos()[0] >= x1 and pg.mouse.get_pos()[0] <= x2 
		and pg.mouse.get_pos()[1] >= y1 and pg.mouse.get_pos()[1] <= y2):
			return True, x1, x2, y1, y2
		return False

	@classmethod	
	def on_quit(cls):
		x1,x2,y1,y2 = 80, 207, 212, 340 
		if (pg.mouse.get_pos()[0] >= x1 and pg.mouse.get_pos()[0] <= x2
		and pg.mouse.get_pos()[1] >= y1 and pg.mouse.get_pos()[1] <= y2):
			return True, x1, x2, y1, y2
		return False

	@classmethod	
	def on_data(cls):
		x1,x2,y1,y2 = 212, 340, 212, 340 
		if (pg.mouse.get_pos()[0] >= x1 and pg.mouse.get_pos()[0] <= x2
		and pg.mouse.get_pos()[1] >= y1 and pg.mouse.get_pos()[1] <= y2):
			return True, x1, x2, y1, y2
		return False


	@classmethod
	def play_clicked(cls, pos): 
		x1,x2,y1,y2 = 80, 340, 80, 207

		if (pos[0] >= x1 and pos[0] <= x2
		and pos[1] >= y1 and pos[1] <= y2): 
			return True
		return False

	@classmethod
	def data_clicked(cls, pos): 
		x1,x2,y1,y2 = 212, 340, 212, 340 

		if (pos[0] >= x1 and pos[0] <= x2
		and pos[1] >= y1 and pos[1] <= y2): 
			return True
		return False


	@classmethod
	def quit_clicked(cls, pos): 
		x1,x2,y1,y2 = 80, 207, 212, 340 

		if (pos[0] >= x1 and pos[0] <= x2
		and pos[1] >= y1 and pos[1] <= y2): 
			return True
		return False


class Leaderboard:
	MAIN_FONT = pg.font.SysFont("Pixeboy", 31)	
	SECOND_FONT = pg.font.SysFont("Pixeboy", 41)
	SECOND_FONT.bold = True

	@classmethod
	def draw_board(cls):
		try:
			with open('stats.dat', 'rb') as stats_read:
				stats = pickle.load(stats_read)

			# DRAWING LEADERBOARD

			WIN.fill((134,19,159))
			run = True
			while run:
				for event in pg.event.get():
					if event.type == pg.QUIT:
						run = False
						pg.quit()
					if event.type == pg.MOUSEBUTTONDOWN:
						pos = pg.mouse.get_pos()
						if cls.back_button_handler(pos):
							run = False


				if type(stats) == list:
					for i in range(1,11):
						if i-1 in range(0, len(stats)): 
							element = cls.MAIN_FONT.render(f"{i}.  {stats[i-1]}", 0, (255,255,255))
							WIN.blit(element, (10, 41*i - 31))
						else:
							element = cls.MAIN_FONT.render(f"{i}.  ---", 0, (255,255,255))
							WIN.blit(element, (10, 41*i - 31))
				else:
					element = cls.MAIN_FONT.render(f"1.  {stats}", 0, (255,255,255))
					WIN.blit(element, (10, 10))

				pg.draw.rect(WIN, (255,255,255), (379, 379, 41, 41))
				back = cls.SECOND_FONT.render("<", 0, (134,19,159))

				x = int(379 + (41 - back.get_width())/2)
				y = int(379 + (41 - back.get_height())/2)
				WIN.blit(back, (x,y))

				a = cls.on_backbutton()
				if a != False:
					width, height = (a[2] - a[1]), (a[4] - a[3])
					tempSurface = pg.Surface((width, height))
					tempSurface.set_alpha(100)
					WIN.blit(tempSurface, (a[1], a[3]))
					pg.draw.rect(WIN, (255,0,0), (a[1], a[3], width, height), 4)




				pg.display.update()

		except FileNotFoundError:
			print("Nie znaleziono pliku")


	@classmethod
	def on_backbutton(cls):
		x1,x2,y1,y2 = 379, 420, 379, 420
		if (pg.mouse.get_pos()[0] >= x1 and pg.mouse.get_pos()[0] <= x2
		and pg.mouse.get_pos()[1] >= y1 and pg.mouse.get_pos()[1] <= y2):
			return True, x1, x2, y1, y2
		return False

	@classmethod
	def back_button_handler(cls, pos):
		if pos[0] >= 379 and pos[0] < 420 and pos[1] >= 379 and pos[1] < 420:
			return True 














# run = True

# while run:
# 	for event in pg.event.get():
# 		if event.type == pg.QUIT:
# 			run = False
# 			pg.quit()
# 		if event.type == pg.MOUSEBUTTONDOWN:
# 			pos = pg.mouse.get_pos()





# 	MainMenu.draw_menu()

	# pg.display.update()
