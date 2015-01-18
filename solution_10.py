# This script prompts the user for an initial odometer reading
# before beginning a road trip, then requests a file including 
# the odometer reading and gallons of gas used (seperated by a
# space).  It then prints out the MPG for each leg of the trip
# and the total MPG for the trip

beginning = eval(input("Please enter your initial odometer reading: "))

while beginning < 0:
	beginning = eval(input("Please enter a valid (positive) odometer reading"))

print ("\nTo calculate your MPG for each leg of your trip, please save the")
print ("odometer reading and gallons of gas used at the end of each leg of")
print ("your trip to a .txt file.  Use a new line for each leg.\n")

fileName = input("What file did you save the information in? ")
inFile = open(fileName,'r')

leg = 1
totalMiles = 0
totalGallons = 0

for line in inFile:
	xStr = line.split(" ")
	ending = eval(xStr [0])
	gallons = eval(xStr [1])
	miles = ending - beginning
	mpg = miles/gallons
	print ("Leg ",leg,": ",mpg," MPG")
	leg +=1
	totalMiles += miles
	totalGallons += gallons
	beginning = ending

totalMPG = totalMiles/totalGallons
print ("Your total MPG for the trip was ",totalMPG)
	