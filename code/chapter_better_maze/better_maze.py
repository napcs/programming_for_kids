# -*- coding: utf-8 -*-

import pygame

class Maze:

	start = ( 0, 0 )
	end = ( 0, 0 )
	user = ( 0, 0 )
	maze = []
	moves = 0
	dirty = []

	user_surface = None
	maze_surface = None

	def __init__ ( self, maze_file ):
		self.load_maze( maze_file )

	def load_maze ( self, maze_file ):

		self.maze = []

		f = open( maze_file, 'r' )
		row = 0
		for line in f:
			col = 0
			self.maze.append( [] )
			for char in line:
				if char == 'S':
					self.start = ( row, col )
				elif char == 'E':
					self.end = ( row, col )
				self.maze[row].append( char )
				col = col + 1
			row = row + 1
		f.close()

		self.size = ( col * 10, row * 10 )

		self.user = self.start

	def init_window ( self ):
		self.window = pygame.display.set_mode( self.size )
		pygame.display.set_caption( 'Maze'  )
		pygame.display.update()

		self.user_surface = pygame.Surface( ( 10, 10 ) )
		self.user_surface.fill( pygame.Color( 255, 255, 255 ) )

		self.maze_surface = pygame.Surface( self.size )

	def render_maze ( self ):
		self.maze_surface.fill( pygame.Color( 0, 0, 0 ) )

		red_block = pygame.Surface( ( 10, 10 ) )
		red_block.fill( pygame.Color( 255, 0, 0 ) )

		green_block = pygame.Surface( ( 10, 10 ) )
		green_block.fill( pygame.Color( 0, 255, 0 ) )

		gray_block = pygame.Surface( ( 10, 10 ) )
		gray_block.fill( pygame.Color( 200, 200, 200 ) )

		row = 0
		for row_data in self.maze:
			col = 0
			for char in row_data:
				if 'S' == char:
					self.maze_surface.blit( red_block, ( col * 10, row * 10 ) )
				elif 'E' == char:
					self.maze_surface.blit( green_block, ( col * 10, row * 10 ) )
				elif ' ' == char:
					pass
				else:
					self.maze_surface.blit( gray_block, ( col * 10, row * 10 ) )
				col = col + 1
			row = row + 1

	def run ( self ):
		self.init_window()
		self.render_maze()

		self.window.blit( self.maze_surface, ( 0, 0, self.size[1], self.size[0] ) )
		self.dirty.append( ( 0, 0, self.size[1], self.size[0] ) )

		self.window.blit( self.user_surface, ( self.start[1] * 10, self.start[0] * 10 ) )

		self.update()

		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					exit()
				elif event.type == pygame.KEYUP:
					goto = self.user

					if event.key == pygame.K_DOWN:
						goto = ( self.user[0]+1, self.user[1] )
					elif event.key == pygame.K_UP:
						goto = ( self.user[0]-1, self.user[1] )
					elif event.key == pygame.K_LEFT:
						goto = ( self.user[0], self.user[1]-1 )
					elif event.key == pygame.K_RIGHT:
						goto = ( self.user[0], self.user[1]+1 )

					if self.maze[goto[0]][goto[1]] == 'E':
						print "You escaped in %d moves!" % self.moves
						pygame.quit()
						exit()
					elif self.maze[goto[0]][goto[1]] != ' ' and self.maze[goto[0]][goto[1]] != 'S':
						goto = self.user

					if self.user != goto:

						self.window.blit( self.user_surface, ( goto[1] * 10, goto[0] * 10 ) )
						self.window.blit( self.maze_surface, ( self.user[1] * 10, self.user[0] * 10 ), ( self.user[1] * 10, self.user[0] * 10, 10, 10 ) )

						self.dirty.append( ( self.user[1] * 10, self.user[0] * 10, 10, 10 ) )
						self.dirty.append( ( goto[1] * 10, goto[0] * 10, 10, 10 ) )

						self.user = goto
						self.moves = self.moves + 1
						pygame.display.set_caption( 'Maze - %d' % self.moves  )

			self.update()

	def update ( self ):
		if 0 != len( self.dirty ):
			pygame.display.update( self.dirty )
			self.dirty = []

if __name__ == '__main__':
	import traceback, sys

	if 1 >= len( sys.argv ):
		print "You must specify a maze file!"
		exit(1)

	try:
		pygame.init()
		maze = Maze( sys.argv[1] )
		maze.run()
	except SystemExit, e:
		pass
	except:
		traceback.print_exc()