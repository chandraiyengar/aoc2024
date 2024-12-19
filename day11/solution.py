stones = [int(num) for num in open('input.txt').read().rstrip().split()]

for step in range(25):
  new_stones = []
  for engraving in stones:
    if engraving == 0: new_stones.append(1)
    elif len(str(engraving)) % 2 == 0:
      left = int(str(engraving)[:len(str(engraving)) // 2]) # // (10 ** (len(str(engraving)) / 2))
      right = int(str(engraving)[len(str(engraving)) // 2:])
      new_stones.append(left)
      new_stones.append(right)
    else:
      new_stones.append(engraving * 2024)
  stones = new_stones
print(len(stones))
