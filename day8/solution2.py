import math
def get_node_locations(first_location, second_location):
  (x1, y1) = first_location
  (x2, y2) = second_location

  gradient = ((x2 - x1) / math.gcd(x2 - x1, y2 - y1), (y2 - y1) / math.gcd(x2 - x1, y2 - y1))
  nodes = set()
  current_location = first_location
  while (current_location[0] >= 0 and current_location[0] < rows and current_location[1] >= 0 and current_location[1] < cols):
    nodes.add(current_location)
    current_location = (current_location[0] - gradient[0], current_location[1] - gradient[1])

  current_location = (first_location[0] + gradient[0], first_location[1] + gradient[1])
  while (current_location[0] >= 0 and current_location[0] < rows and current_location[1] >= 0 and current_location[1] < cols):
    nodes.add(current_location)
    current_location = (current_location[0] + gradient[0], current_location[1] + gradient[1])

  return nodes

map = open('input.txt','r').readlines()

antenna_locations = {}
node_locations = set()
rows = len(map)
cols = len(map[0].rstrip())
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
      nodes = get_node_locations(first_location, second_location)
      for x in nodes:
        node_locations.add(x)

print(len(node_locations))
