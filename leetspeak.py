string = input('Enter some text: ')

for char in string:
	if char == 'a':
		string = string.replace('a','4')
	elif char == 'e':
		string = string.replace('e','3')
	elif char == 'g':
		string = string.replace('g','6')
	elif char == 'i':
		string = string.replace('i','1')
	elif char == 'o':
		string = string.replace('o','0')
	elif char == 's': 
		string = string.replace('s','5')
	elif char == 't':
		string = string.replace('t','7')
	else:
		pass

print(string)