from Gomok import *
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)
game = Gomok()

@app.route('/Gomok', methods = ['GET','POST'])
def Gomok():
	global game
	if request.method == 'POST':
		x = request.json['x']
		y = request.json['y']
		game.put_point(x, y)
		x, y = game.get_point()
		return jsonify({'x' : x, 'y' : y})

	elif request.method == 'GET':
		html = ''
		board = np.full((15,15), '□')
		for i, pt in enumerate(game.get_board()):
			board[pt[1], pt[0]] = '■' if i % 2 is not 0 else '▲'
		for i in range(15):
			html = html + ' '.join(board[i]) + '<br>'
		return html

	

if __name__ == '__main__':
	game.get_point()
	app.run(debug = True)