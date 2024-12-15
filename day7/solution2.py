def canBeMade(target, values):
  print("target:", target, "values:", values)
  if len(values) == 1: return target == values[0]
  else: 
    return canBeMade(target - values[-1], values[:-1]) or (target % values[-1] == 0 and canBeMade(target / values[-1], values[:-1])) or ((target - values[-1]) % (10**len(str(values[-1]))) == 0 and canBeMade((target - values[-1]) / 10**len(str(values[-1])), values[:-1]))

file = open('input.txt','r').readlines()

total = 0

for line in file:
  print("line:", line)
  target, others = line.split(':')
  values = [int(x) for x in others.rstrip().split()]
  if canBeMade(int(target), values):
    total += int(target)
  
print(total)