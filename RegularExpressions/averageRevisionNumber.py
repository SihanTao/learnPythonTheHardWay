import re

filename = input("Enter file:")
mbox = open(filename)
sum = 0
count = 0
for line in mbox:
    line = line.rstrip()
    x_int = [int(x) for x in re.findall('^New Revision: ([0-9]+)', line)]
    for i in x_int:
        sum += i
        count += 1

print(sum // count)
