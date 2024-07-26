import sys
import re
pattern = r"\\"
for line in sys.stdin:
    line = line.rstrip()
    if line:
        line = re.sub(r"\b(A|a)(A|a)*\b", "argh", line, 1,0)
        print(line)
    else:
        break
