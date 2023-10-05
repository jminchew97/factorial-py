def factorial(num):
	# your code here
	factorial = 1
	for i in reversed(range(1, num+1)):		
		factorial *= i
	return factorial
