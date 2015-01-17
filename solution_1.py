#this script prompts the user for a number "n", then returns the nth number in the Fibonacci sequence
def fib(nth):
	last = 0
	total = 1
	for i in range(nth):
		total += last
		last = total-last
	return total


n = eval(input("Enter a number, n, to see the nth Fibonacci number"))
print (fib(n-1))