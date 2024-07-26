import sys
import re
pattern = r"((0)|(10((00|1)*)01)|(11))*"

for line in range(0,500):
    line = bin(line)[2:]
    print(line, '--', int(line, 2), '--', re.fullmatch(pattern, line))