file = open('input.txt','r').readlines()

arr = [[0 for i in range(len(file))] for j in range(len(file[0]))]
current_position = [0,0]
total = 1
for i in range(len(file)):
  for j in range(len(file[i].rstrip())):
    arr[i][j] = file[i][j]
    if not (arr[i][j] in {'.', '#'}):
      current_position = [i,j]
      current = arr[i][j]

while not ((current_position[0] in {0, len(file) - 1}) or (current_position[1] in {0, len(file[0]) - 1})):
  print(current_position, current)
  if current == '^' and arr[current_position[0] - 1][current_position[1]] == '#':
    current = '>'
    continue
  if current == '^':
    current_position = [current_position[0] - 1, current_position[1]]
    if arr[current_position[0]][current_position[1]] == '.':
      total += 1
      arr[current_position[0]][current_position[1]] = 'X'
    continue
  if current == '>' and arr[current_position[0]][current_position[1] + 1] == '#':
    current = 'v'
    continue
  if current == '>':
    current_position = [current_position[0], current_position[1] + 1]
    if arr[current_position[0]][current_position[1]] == '.':
      total += 1
      arr[current_position[0]][current_position[1]] = 'X'
    continue
  if current == 'v' and arr[current_position[0] + 1][current_position[1]] == '#':
    current = '<'
    continue
  if current == 'v':
    current_position = [current_position[0] + 1, current_position[1]]
    if arr[current_position[0]][current_position[1]] == '.':
      total += 1
      arr[current_position[0]][current_position[1]] = 'X'
    continue
  if current == '<' and arr[current_position[0]][current_position[1] - 1] == '#':
    current = '^'
    continue
  if current == '<':
    current_position = [current_position[0], current_position[1] - 1]
    if arr[current_position[0]][current_position[1]] == '.':
      total += 1
      arr[current_position[0]][current_position[1]] = 'X'
    continue

print(total)