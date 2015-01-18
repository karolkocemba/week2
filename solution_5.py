#This script checks if a number entered by the user is a prime number
import math
def prime(n):
	if type(n) != int:
		print ("That is not an integer /n")
	elif n <= 2:
		print ("Make sure your integer is positive and greater than 2:")
	else:
		is_prime = True
		for i in range(2,n):
			# although the definition of 'prime' in the problem calls to check for 
			# divisibility by 2 through the SQRT of n, I ran the loop through n itself
			# because if n has a perfect square if WILL by definition be divisible by
			# it and the if statement below will break anyway
			# This seemed easier than importing the math library and then accounting for
			# square roots that are not integers breaking the for loop
			if n%i == 0:
				print (n," is divisible ",i,", therefore, it is not prime")
				is_prime = False
				break
		if is_prime:
			print(n," is a prime number")

prime(eval(input("Enter a positive integer greater than 2 to see if it is prime: ")))