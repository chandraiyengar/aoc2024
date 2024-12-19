from time import perf_counter
stones = [int(num) for num in open('input.txt').read().rstrip().split()]

for step in range(75):
  t_start = perf_counter()
  new_stones = []
  for engraving in stones:
    if engraving == 0: new_stones.append(1)
    elif (engraving_length := len(engraving_string := str(engraving))) % 2 == 0:
      left = int(engraving_string[:engraving_length // 2]) # // (10 ** (len(str(engraving)) / 2))
      right = int(engraving_string[engraving_length // 2:])
      new_stones.append(left)
      new_stones.append(right)
    else:
      new_stones.append(engraving * 2024)
  stones = new_stones
  print("length stones: ", len(stones), "step: ", step)
  t_end = perf_counter()
  print("Elapsed time:", t_end - t_start,"s")
print(len(stones))
