disk_map = open('input.txt','r').read().rstrip()

disk = []
id = 0
is_file = True
# put input into a list
for char in disk_map:
  if is_file:
    disk.extend([id for _ in range(int(char))])
    id += 1
    is_file = not is_file
    continue
  else:
    disk.extend(['.' for _ in range(int(char))])
    is_file = not is_file
    continue
# remove last elements if they are .'s
while disk[-1] == '.':
  disk.pop()
# iterate through moving back numbers to the dots
pointer1 = disk.index('.')
while pointer1 < len(disk) and disk[pointer1] == '.':
  disk[pointer1] = disk[-1]
  disk.pop()
  while disk[-1] == '.':
    disk.pop()
  pointer1 += 1
  while pointer1 < len(disk) and not disk[pointer1] == '.':
    pointer1 += 1
checksum = sum(index * num for index, num in enumerate(disk))
print(checksum)
