def factorial1(n):
	try:
                if n < 0:
			raise ValueError()
		elif n == 0:
			return(1)
		else:
			y = 1
			for x in range(1, n+1):
				y = y * x
			return(y)
	except ValueError:
		print('Please Try Again with a Non-Negative Number')

def factorial2(n):
	facts = []
	try:
		if n < 0:
			raise ValueError()
		for a in range(n+1):
			facts.append(factorial1(a))
	except ValueError:
		print('Please Try Again with a Non-Negative Number')
	return facts

