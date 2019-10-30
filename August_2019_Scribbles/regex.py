import re

text = open('file.txt')
for line in text:
    line.rstrip()
    if re.search('^F..m:.+', line):
        print(line)