import re
def calculate(data:dict, text:str):
	a = data["a"]
	b = data["b"]
	c = data["c"]
	pattern = re.compile('[a-c]{1}[+-]?={1}[a-c]?[+-]?\d*')
	matches = re.findall(pattern, text)
	for records in matches:
		if records[0:1] == 'a':
			if records[1:2] == '+':
				a += eval(records[3:])
			elif records[1:2] == '-':
				a -= eval(records[3:])
			else:
				a = eval(records[2:])
		elif records[0:1] == 'b':
			if records[1:2] == '+':
				b += eval(records[3:])
			elif records[1:2] == '-':
				b -= eval(records[3:])
			else:
				b = eval(records[2:])
		else:
			if records[1:2] == '+':
				c += eval(records[3:])
			elif records[1:2] == '-':
				c -= eval(records[3:])
			else:
				c = eval(records[2:])
	data = {'a':a, 'b':b, 'c':c}
	return data
				
