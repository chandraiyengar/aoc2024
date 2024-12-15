file = open('input.txt','r').readlines()
total = 0
pairs = {}

for line in file:
  if '|' in line:
    x1, x2 = line.rstrip().split('|')
    pairs[x1] = pairs.get(x1,[])
    pairs[x1].append(x2)
  else:
    to_test = line.rstrip().split(',')
    isValid = True
    for index in range(len(to_test)-1, -1, -1):
      s = to_test[index]
      if s in pairs:
        p = pairs[s]
      else: break
      for i in range(index):
        if to_test[i] in p:
          isValid = False
          break
      if not isValid:
        break
      if index == 0:
        total += int(to_test[len(to_test) // 2])

print(total)



