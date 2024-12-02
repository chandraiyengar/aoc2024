f = open('input.txt', 'r')
total = 0

for str_line in f:
  line = [int(item) for item in str_line.split()]
  isIncreasing = True
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
      break
    if abs(line[i] - line[i + 1]) == 0 or abs(line[i] - line[i + 1]) > 3:
      break

print(total)
