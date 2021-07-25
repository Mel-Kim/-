Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def Stack():
	stack = []

	
>>>  def Stack():
	stack = []
	
SyntaxError: unexpected indent
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
================================ RESTART: Shell ================================
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