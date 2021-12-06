import re

hand = open('mbox-short.txt')
out = open('re01-output.txt', 'w')

for line in hand:
    line = line.strip()
    if re.search('From:', line):
        out.write(line + '\n')
