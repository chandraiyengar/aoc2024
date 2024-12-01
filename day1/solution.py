f = open('input.txt', 'r')
leftList = []
rightList = []

for line in f:
  x = line.split()
  leftList.append(x[0])
  rightList.append(x[1])
total = 0
rightList.sort()
leftList.sort()
for x in range(len(leftList)):
  total += abs(int(leftList[x]) - int(rightList[x]))

print(total)
