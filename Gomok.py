from console_pipe import *

class Gomok():
	def __init__(self):
		self.pipe = console_pipe('Yixin.exe')
		self.pipe.write(b'START 15\r\nBEGIN\r\n')
		self.marks = []

	def __del__(self):
		self.pipe.write(b'END\r\n')
		self.pipe.close()

	def get_point(self):
		text = 'a'
		while not text[0].isdecimal():
			text = self.pipe.read(1024)[1].decode('utf-8')
		idx = text.find(',')
		x = int(text[0:idx])
		y = int(text[idx + 1 : len(text)])
		self.marks.append((x,y))
		return (x, y)

	def put_point(self, x, y):
		self.pipe.write('TURN {},{}\r\n'.format(x, y).encode('utf-8'))
		self.marks.append((x,y))

	def restart_game(self):
		self.pipe.wrtie(b'RESTART\r\nBEGIN\r\n')
		self.marks = []

	def get_board(self):
		return self.marks
