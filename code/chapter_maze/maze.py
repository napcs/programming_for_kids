# -*- coding: utf-8 -*-

import curses

class Maze:

	start = ( 0, 0 )
	end = ( 0, 0 )
	user = ( 0, 0 )
	maze = []
	moves = 0

	def __init__ ( self, stdscr, maze_file=None ):
		self.scr = stdscr
		self.load_maze( maze_file )

	def load_maze ( self, maze_file ):

		self.scr.clear()
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

		self.user = self.start
		self.render_maze()

	def render_maze ( self ):
		row = 0
		for row_data in self.maze:
			col = 0
			for char in row_data:
				self.scr.addstr( row + 2, col, char )
				col = col + 1
			row = row + 1
		self.scr.addstr( self.user[0] + 2, self.user[1], "*" )
		self.scr.move( 0, 0 )
		self.scr.refresh()

	def main ( self ):
		self.scr.addstr( 0, 0, "Welcome To Maze!  Arrow keys move, Q to quit." )

		while True:
			goto = None
			c = self.scr.getch()
			if 0 < c < 256:
				c = chr( c )
				if c in 'Qq' : break
				else: pass
			elif c == curses.KEY_UP:
				goto = ( self.user[0]-1, self.user[1] )
			elif c == curses.KEY_DOWN:
				goto = ( self.user[0]+1, self.user[1] )
			elif c == curses.KEY_LEFT:
				goto = ( self.user[0], self.user[1]-1 )
			elif c == curses.KEY_RIGHT:
				goto = ( self.user[0], self.user[1]+1 )
			else: pass

			if self.maze[goto[0]][goto[1]] == 'E':
				self.scr.clear()
				self.scr.refresh()
				self.scr.addstr( 0, 0, "You escaped in %d moves! Hit any key to quit." % self.moves )
				c = self.scr.getch()
				break
			elif self.maze[goto[0]][goto[1]] == ' ' or self.maze[goto[0]][goto[1]] == 'S':
				self.user = goto
				self.moves = self.moves + 1

			self.render_maze()

if __name__ == '__main__':
	import traceback, sys

	if 1 >= len( sys.argv ):
		print "You must specify a maze file!"
		exit(1)

	try:
		stdscr = curses.initscr()
		curses.noecho() ; curses.cbreak()
		stdscr.keypad( 1 )
		maze = Maze( stdscr, sys.argv[1] )
		maze.main()
		# Set everything back to normal
		stdscr.keypad( 0 )
		curses.echo() ; curses.nocbreak()
		curses.endwin()
	except:
		stdscr.keypad( 0 )
		curses.echo() ; curses.nocbreak()
		curses.endwin()
		traceback.print_exc()
