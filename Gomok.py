from console_pipe import *

class Gomok():
	def __init__(self):
		self.marks = []
		self.playing = False

	def __del__(self):
		self.end_game()

	def get_point(self):
		text = 'a'
		while not text[0].isdecimal():
			text = self.pipe.read(1024)[1].decode('utf-8')
		idx = text.find(',')
		x = int(text[0:idx])
		y = int(text[idx + 1 : len(text)])
		self.marks.append((x,y))
		print(x, y)
		return (x, y)

	def put_point(self, x, y):
		self.pipe.write('TURN {},{}\r\n'.format(x, y).encode('utf-8'))
		self.marks.append((x,y))

	def start_game(self):
		self.pipe = console_pipe('Yixin.exe')
		self.pipe.write(b'START 15\r\nBEGIN\r\n')
		self.marks = []
		self.playing = True

	def restart_game(self):
		self.pipe.wrtie(b'RESTART\r\nBEGIN\r\n')
		self.marks = []
		self.playing = True

	def end_game(self):
		self.pipe.write(b'END\r\n')
		self.pipe.close()
		self.marks = []
		self.playing = False
		print('remove process success')

	def get_board(self):
		return self.marks

	def is_playing(self):
		return self.playing