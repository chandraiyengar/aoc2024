import re

file = open('input.txt','r').readlines()

# first check for horizontal matches
total = 0
prev_line = []
for index, line in enumerate(file):
  total += len(re.findall('XMAS', line))
  total += len(re.findall('SAMX', line))

rotate_file = ['' for i in range(len(file))]
for line in file:
  for index, char in enumerate(line.rstrip()):
    rotate_file[index] += char

for line in rotate_file:
  total += len(re.findall('XMAS', line))
  total += len(re.findall('SAMX', line))

rotate_file = ['' for i in range(len(file) * 2)]
for line_number, line in enumerate(file):
  for index, char in enumerate(line_number * '.' + line.rstrip()):
    rotate_file[index] += char

for line in rotate_file:
  total += len(re.findall('XMAS', line))
  total += len(re.findall('SAMX', line))

rotate_file = ['' for i in range(len(file) * 2)]
for line_number, line in enumerate(file):
  for index, char in enumerate((len(file) - line_number) * '.' + line.rstrip()):
    rotate_file[index] += char

for line in rotate_file:
  total += len(re.findall('XMAS', line))
  total += len(re.findall('SAMX', line))



print(total)

