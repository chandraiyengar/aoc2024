from time import perf_counter
import math
stones = [int(num) for num in open('input.txt').read().rstrip().split()]
stones_dict = {}
for engraving in stones:
  occurences = stones_dict.get(engraving, 0)
  occurences += 1
  stones_dict[engraving] = occurences

for step in range(75):
  t_start = perf_counter()
  new_stones_dict = {}
  for engraving in stones_dict:
    if engraving == 0: 
      occurences = new_stones_dict.get(1, 0)
      occurences += stones_dict[engraving]
      new_stones_dict[1] = occurences
    elif len(str(engraving)) % 2 == 0:
      left = int(str(engraving)[:len(str(engraving)) // 2])
      right = int(str(engraving)[len(str(engraving)) // 2:])
      occurences_left = new_stones_dict.get(left, 0)
      occurences_left += stones_dict[engraving]
      new_stones_dict[left] = occurences_left
      occurences_right = new_stones_dict.get(right, 0)
      occurences_right += stones_dict[engraving]
      new_stones_dict[right] = occurences_right
    else:
      occurences = new_stones_dict.get(engraving * 2024, 0)
      occurences += stones_dict[engraving]
      new_stones_dict[engraving * 2024] = occurences
  stones_dict = new_stones_dict
  t_end = perf_counter()
  print("Elapsed time:", t_end - t_start,"s")
print(sum([stones_dict[x] for x in (stones_dict)]))
