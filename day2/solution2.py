f = open('input.txt', 'r')
total = 0
for str_line in f:
  line = [int(item) for item in str_line.split()]
  isIncreasing = True
  doublecheck = []
  for i in range(len(line)):
    if (len(line) < 2):
      total += 1
      break
    if i == len(line) - 1:
      total += 1
      break
    if i == 0:
      isIncreasing = line[i] - line[i + 1] < 0
    if (line[i] - line[i + 1] < 0) != isIncreasing:
      doublecheck.append(line[:i - 1] + line[i:])
      doublecheck.append(line[:i] + line[i + 1:])
      doublecheck.append(line[:i + 1] + line[i + 2:])
      break
    if abs(line[i] - line[i + 1]) == 0 or abs(line[i] - line[i + 1]) > 3:
      doublecheck.append(line[:i - 1] + line[i:])
      doublecheck.append(line[:i] + line[i + 1:])
      doublecheck.append(line[:i + 1] + line[i + 2:])
      break
  addSum = 0
  print(doublecheck)
  for line in doublecheck:
    for i in range(len(line)):
      if (len(line) < 2):
        addSum += 1
        break
      if i == len(line) - 1:
        addSum += 1
        break
      if i == 0:
        isIncreasing = line[i] - line[i + 1] < 0
      if (line[i] - line[i + 1] < 0) != isIncreasing:
        break
      if abs(line[i] - line[i + 1]) == 0 or abs(line[i] - line[i + 1]) > 3:
        break
  addSum = 1 if (addSum > 0) else 0
  total += addSum

print(total)
