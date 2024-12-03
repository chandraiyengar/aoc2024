import re

file = open('input.txt','r')
matches = []

for line in file:
  matches.append(re.findall("mul\([0-9]+,[0-9]+\)|don't\(\)|do\(\)", line))

total = 0
isDo = True

for linearray in matches:
  for match in linearray:
    if match == "don't()":
      isDo = False
      continue
    if match == "do()":
      isDo = True
      continue
    if isDo == False:
      continue 
    a, b = re.findall("[0-9]+", match)
    total += int(a) * int(b)

print(total)
