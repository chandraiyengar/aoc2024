import re

file = open('input.txt','r')
matches = []

for line in file:
  matches.append(re.findall("mul\([0-9]+,[0-9]+\)", line))

total = 0

for linearray in matches:
  for match in linearray:
    a, b = re.findall("[0-9]+", match)
    total += int(a) * int(b)

print(total)
