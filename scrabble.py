from flask import Flask
from flask import render_template

app = Flask(__name__)

board = [['' for i in range(15)] for j in range(15)]
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

# special score ids
tw = [0, 7, 14, 105, 119, 210, 217, 224]
tl = [20, 24, 76, 80, 84, 88, 136, 140, 144, 148, 200, 204]
dw = [16, 28, 32, 42, 48, 56, 64, 70, 154, 160, 168, 176, 182, 192, 196, 208]
dl = [3, 11, 36, 38, 45, 52, 59, 92, 96, 98, 102, 108, 116, 122, 126, 128, 132, 165, 172, 179, 186, 188, 213, 221]

@app.route('/')
def home():
	for i in range(15):
		for j in range(15):
			if i + j*15 in tw:
				board[i][j] = 'TRIPLE\nWORD\nSCORE'
			elif i + j*15 in tl:
				board[i][j] = 'TRIPLE\nLETTER\nSCORE'
			elif i + j*15 in dw:
				board[i][j] = 'DOUBLE\nWORD\nSCORE'
			elif i + j*15 in dl:
				board[i][j] = 'DOUBLE\nLETTER\nSCORE'
			elif i + j*15 == 112:
				board[i][j] = '☆'

	return render_template('board.html', currBoard=board, letters=letters)