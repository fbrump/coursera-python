# exercise
"""
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
"""
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
lst = list()
dic = dict()
tpl = tuple()
for line in handle:
    if (line.startswith('From ')):
        time = line.split()[5]
        hour = time.split(':')[0]
        val = dic.get(hour)
        if val == None:
            dic[hour] = 1
        else:
            dic[hour] = val + 1
# adiciono na lista
for k, v in dic.items():
    lst.append((k, v))
lst.sort()
for k, v in lst:
    print k, v