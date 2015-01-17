
def fib(nth):
	last = 0
	total = 1
	for i in range(nth):
		total += last
		last = total-last
	return total


n = eval(input("Enter a number, n, to see the nth Fibonacci number"))
print (fib(n-1))