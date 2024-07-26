import sys
import re
pattern = r".*(\b|/B)cat(\b|/B).*"
result = []
for line in sys.stdin:
    line = line.rstrip()
    if line != '':
        if re.match(pattern, line):
            result += [line]
    else:
        break
print(*result, sep='\n')