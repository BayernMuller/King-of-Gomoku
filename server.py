from gomok import *
import numpy as np
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
game = Gomok()

def shape_board():
	board = np.full((15,15), '┼')
	board[0, 0] = '┌'; board[14,0] = '└'; board[0,14] = '┐'; board[14,14] = '┘'
	for i in range(1, 14):
		board[14, i] = '┴'; board[0,i] = '┬'; board[i,0]='├'; board[i,14] = '┤'
	return board

@app.route('/Gomoku', methods = ['GET','POST'])
def Gomok():
	global game
	if request.method == 'POST':
		state = request.json['state']
		if state == 'RESTART':
			game.restart_game()
			game.get_point()
			return 'The game is restarted.'

		elif state == 'END':
			game.end_game()
			return 'The game is done.'

		elif state == 'START':
			game.start_game()
			game.get_point()
			return 'The game is started.'

		elif state == 'TURN':
			x = request.json['x']
			y = request.json['y']
			game.put_point(x, y)
			x, y = game.get_point()
			return jsonify({'x' : x, 'y' : y})

		else:
			return 'wrong post.'

	elif request.method == 'GET':
		board = shape_board()
		for i, pt in enumerate(game.get_board()):
			board[pt[1], pt[0]] = '●' if i % 2 is 0 else '○'
		if not game.is_playing():
			msg = 'The game is not started.'
		else: 
			msg = 'Human\'s turn.' if len(game.get_board()) % 2 is not 0 else 'Ai\'s turn.'
		return render_template('index.html', board=board, msg=msg)


if __name__ == '__main__':
	app.run(debug = True)
	print('End server')