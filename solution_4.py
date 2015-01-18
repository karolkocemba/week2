#this program prompts the user for a beginning number on which to run the Syracuse sequence
def syr (x):
	while x != 1:
		if x%2 == 0:
			print (int(x))
			x /= 2
		else:
			print (int(x))
			x = 3*x+1
	print (1)

syr(eval(input("Enter a natural number to run the Syracuse sequence on")))





