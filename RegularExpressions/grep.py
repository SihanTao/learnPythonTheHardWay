import re

regular_expression = input("Enter a regular expression: ")
file_name = 'mbox.txt'
mbox = open(file_name)

count = 0
for line in mbox:
    line = line.rstrip()
    x = re.findall(regular_expression, line)
    if len(x) > 0:
        count = count + 1

print(f"{file_name} had {count} lines that matched {regular_expression}")
