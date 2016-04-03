"""
5.2 Write a program that repeatedly prompts a 
user for integer numbers until the user enters 
'done'. Once 'done' is entered, print out the 
largest and smallest of the numbers. If the user 
enters anything other than a valid number catch 
it with a try/except and put out an appropriate 
message and ignore the number. Enter the numbers 
from the book for problem 5.1 and Match the desired 
output as shown.
"""
largest = None
smallest = None
try:
	while True:
		num = int(raw_input("Enter a number: "))
		# Validate of the must largest number
		if (largest is None):
			largest = num
		elif(num > largest):
			largest = num
		# Validate of the must smallest number
		if (smallest is None):
			smallest = num
		elif (num < smallest):
			smallest = num
		# Finelly code
		if num == "done":
			break
		#print num
except Exception, e:
	print("Invalid input")
	#raise e
print "Maximum is", largest
print "Minimum is", smallest