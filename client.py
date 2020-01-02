import requests, json
url = 'http://localhost:5000/Gomok'
headers = {'Content-Type' : 'application/json; charset=utf-8'}
while True:
	x = int(input('x : '))
	y = int(input('y : '))
	data = {'x' : x, 'y' : y }
	res = requests.post(url, headers = headers, data=json.dumps(data))
	print(res.text)