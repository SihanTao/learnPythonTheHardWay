import re

hand = open('mbox-short.txt')
out = open('re03-output.txt', 'w')

for line in hand:
    line = line.strip()
    if re.search('^F..m:', line):
        out.write(line + '\n')
