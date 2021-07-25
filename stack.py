>>> def Stack():
	stack = []
	stack.append(1)
	stack.append(2)
	stack.append(3)
	stack.append(4)
	stack.append(5)
	print(stack)
	while stack:
		print("POP Value is", stack.pop())

		
>>> Stack()
[1, 2, 3, 4, 5]
POP Value is 5
POP Value is 4
POP Value is 3
POP Value is 2
POP Value is 1
>>> 
