__author__ = 'brianwhitney'

with open("day9.txt") as charfile:
    line = charfile.readline()
    parsed_val = []
    in_garbage = False
    b = 0
    total = 0
    skipnext = False
    for i in range(0, len(line)):
        if skipnext:
            skipnext = False
            continue
        if line[i] == "!":
            skipnext = True
            continue
        if line[i] == "<" and not in_garbage:
            in_garbage = True
            continue
        if line[i] == ">" and in_garbage:
            in_garbage = False
            continue
        if in_garbage:
            parsed_val.append(line[i])
            continue
        if line[i] == "}" or line[i] == "{":
            if line[i] == "{":
                b = b + 1
            if line[i] == "}":
                total = total + b
                b = b - 1
    print("The length of garbage is {}".format(str(len(parsed_val))))
    print("The total value of this is: {}".format(str(total)))