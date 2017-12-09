__author__ = 'brianwhitney'

import re

with open("day2.txt") as csvfile:
    sum = 0
    sum2 = 0
    for line in csvfile:
        values = re.findall("\d+", line)
        int_vals = []
        for value in values:
            int_vals.append(int(value))
        sum = sum + (max(int_vals) - min(int_vals))
        found = False
        for i in range(0, len(int_vals)):
            for j in range(0, len(int_vals)):
                val = float(int_vals[i]) / float(int_vals[j])
                if val > 0.0 and not re.search("\.0*[1-9][0-9]*",str(val)) and i != j:
                    sum2 = sum2 + int(val)
                    found = True
                    break
            if found:
                break

    print str(sum)
    print str(sum2)