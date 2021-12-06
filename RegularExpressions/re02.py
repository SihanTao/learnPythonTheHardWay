import re

hand = open('mbox-short.txt')
out = open('re02-output.txt', 'w')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):
        out.write(line + '\n')
