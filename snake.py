def main():
	import pygame as pg
	import time, random
	pg.init()
	cube_size, disp_w, disp_h = 20, 800, 600
	screen = pg.display.set_mode((disp_w,disp_h))
	pg.display.set_caption('Snake')
	coords, ingame, eaten, snakeLength, snakeList, move = [
            (disp_w/2-cube_size/2)//cube_size*cube_size, (disp_h-3*cube_size)//cube_size*cube_size], True, True, 1, [], 'up'
	while ingame:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				quit()
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_RIGHT and move != 'left': move = 'right'
				elif event.key == pg.K_LEFT and move != 'right': move = 'left'
				elif event.key == pg.K_UP and move != 'down': move = 'up'
				elif event.key == pg.K_DOWN and move != 'up': move = 'down'
				elif event.key == pg.K_q:
					pg.quit()
					quit()
		if move == 'right': coords[0] += cube_size
		elif move == 'left': coords[0] -= cube_size
		elif move == 'up': coords[1] -= cube_size
		elif move == 'down': coords[1] += cube_size
		snakeHead = []
		snakeHead.append(coords[0])
		snakeHead.append(coords[1])
		snakeList.append(snakeHead)
		if len(snakeList) > snakeLength: del snakeList[0]
		if eaten:
			apple = [random.randrange(0,disp_w-cube_size,cube_size), random.randrange(0,disp_h-cube_size,cube_size)]
			eaten = False#//cube_size*cube_size
		screen.fill((255,255,255))
		if coords[0] < 0 or coords[0]+cube_size > disp_w or coords[1] < 0 or coords[1]+cube_size > disp_h: ingame = False
		if coords == apple:#[0] >= apple[0] and coords[0]+cube_size <= apple[0] and coords[1] >= apple[1] and coords[1]+cube_size <= apple[1]:
			snakeLength += 1
			eaten = True
		for bodypart in snakeList: pg.draw.rect(screen, (0,210,0), [bodypart[0],bodypart[1],cube_size,cube_size])
		for bodypart in snakeList[:-1]:
			if bodypart == snakeHead: ingame = False
		pg.draw.rect(screen, (210,0,0), (apple[0], apple[1], cube_size, cube_size))
		pg.draw.rect(screen, (0,155,0), (coords[0], coords[1], cube_size, cube_size))
		pg.display.update()
		pg.time.wait(200)

if __name__ == '__main__':
	main()
