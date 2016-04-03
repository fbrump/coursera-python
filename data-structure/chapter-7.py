# Open
xfile = open('mbox.txt')

# Read
count = 0
for line in xfile:
	count = count + 1

print ('line count', count)
# Write

# Close

"""
	Reading the *Whole* File
"""
fhand = open('mbox-short.txt')
inp = fhand.read()
print (inp)

"""
	Searching Through a File
"""

fhand = open('mbox-short.txt')
for line in fhand:
	if (line.startswith('From:')):
		print (line)
