def trailscore(start_row, start_col, row, col, previous_height):
  new_height = topographic_map[row][col]
  # print("row:", row, "col:", col,"new height:", new_height, "previous height:", previous_height)
  if new_height - previous_height == 1:
    if new_height == 9: 
      if ((start_row, start_col) in trails) and (row, col) in trails[(start_row, start_col)]: return 0
      else:
        trails.setdefault((start_row, start_col), []).append((row, col))
        return 1
    total = 0
    if row > 0: total += trailscore(start_row, start_col, row - 1, col, new_height)
    if row < map_rows - 1: total += trailscore(start_row, start_col, row + 1, col, new_height)
    if col > 0: total += trailscore(start_row, start_col, row, col - 1, new_height)
    if col < map_cols - 1: total += trailscore(start_row, start_col, row, col + 1, new_height)
    return total
  else: return 0



topographic_map = [[int(num) for num in string_line.rstrip()] for string_line in open('input.txt','r').readlines()]
print(topographic_map)
map_rows = len(topographic_map)
map_cols = len(topographic_map[0])
trails = {}

total_trails = 0
for row, line in enumerate(topographic_map):
  for col, height in enumerate(line):
    if height == 0:
      print(row, col, trailscore(row, col, row, col, -1))
      trails[(row, col)] = []
      total_trails += trailscore(row, col, row, col, -1)

print(total_trails)



