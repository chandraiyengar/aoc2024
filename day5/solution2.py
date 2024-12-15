class CustomSortable:
    def __init__(self, value):
        self.value = value
    
    def __lt__(self, other):
        return other.value in pairs.get(self.value, [])

file = open('input.txt','r').readlines()
total = 0
pairs = {}
pairs_rev = {}

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
        items = [CustomSortable(x) for x in to_test]
        sorted_items = sorted(items)
        total += int(sorted_items[len(sorted_items) // 2].value)
        print([x.value for x in sorted_items])
        break

print(total)



