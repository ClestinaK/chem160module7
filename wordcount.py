import sys
from collections import Counter
from os import path
filename = input("Enter the name of the file: woods.txt")
if not os.path.exists(filename):
    sys.exit("Cannot find file given")
file = open(filename, "r")
words = []
while 1:
    line = file.readline()      #Read next line from stdin into "line"
    if line == "":              #Quit while loop if line is empty
        break
    words.extend(line.split())
counts = Counter(words)
words_lower = []
for i in words:
    words_lower.append(i.lower())
words = words_lower
for i in counts:
    print("%2d: %s" %(counts[i], i))