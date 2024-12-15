import re

file = open('input.txt','r').readlines()

# first check for horizontal matches

total = 0
for line_number,line in enumerate(file):
  for index, character in enumerate(line):
    if character == 'A' and (index - 1 >= 0 and index + 1 < len(line)) and (line_number - 1 >= 0 and line_number + 1 < len(file)):
        seen_chars = []
        seen_chars.append(file[line_number - 1][index - 1])
        seen_chars.append(file[line_number + 1][index + 1])
        seen_chars_d = []
        seen_chars_d.append(file[line_number - 1][index + 1])
        seen_chars_d.append(file[line_number + 1][index - 1])
        if seen_chars.count('S') == 1 and seen_chars.count('M') == 1 and seen_chars_d.count('S') == 1 and seen_chars_d.count('M') == 1:
           total += 1

print(total)

