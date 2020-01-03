import requests, json
url = 'http://localhost:5000/Gomoku'
headers = {'Content-Type' : 'application/json; charset=utf-8'}
x = 0; y = 0;
while True:
	state = input('state : ')
	if state == 'TURN':
		x = int(input('x : '))
		y = int(input('y : '))
	data = {'x' : x, 'y' : y, 'state' : state }
	res = requests.post(url, headers = headers, data=json.dumps(data))
	print(res.text)