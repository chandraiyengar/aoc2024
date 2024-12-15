def get_node_locations(first_location, second_location):
  (x1, y1) = first_location
  (x2, y2) = second_location

  return ((2 * x1 - x2, 2 * y1 - y2), (2 * x2 - x1, 2 * y2 - y1))

map = open('input.txt','r').readlines()

antenna_locations = {}
node_locations = set()
total = 0

for row_index, line in enumerate(map):
  for col_index, ch in enumerate(line.rstrip()):
    if (ch != '.'): 
      locations = antenna_locations.setdefault(ch, [])
      locations.append((row_index, col_index))
      antenna_locations[ch] = locations

for antenna_type in antenna_locations.keys():
  for first_location in antenna_locations[antenna_type]:
    for second_location in antenna_locations[antenna_type]:
      if first_location == second_location:
        continue
      two_nodes = get_node_locations(first_location, second_location)
      for x in two_nodes:
        if (x[0] >= 0 and x[0] < len(map) and x[1] >= 0 and x[1] < len(map[0].rstrip())): node_locations.add(x)

print(len(node_locations))
