f = open('input.txt', 'r')
leftList = []
rightList = []

for line in f:
  x = line.split()
  leftList.append(x[0])
  rightList.append(x[1])
total = 0

dict = {}
for x in range(len(rightList)):
  value = dict.setdefault(int(rightList[x]), 0)
  dict[int(rightList[x])] = value + 1

for x in range(len(leftList)):
  total += int(leftList[x]) * dict.get(int(leftList[x]), 0)


print(total)
