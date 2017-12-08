

jumplist = []
with open("day5.txt") as jumpinstructions:
    for jumpinstruction in jumpinstructions:
        jumplist.append(int(jumpinstruction))

jump = 0
iteration = 0
while jump < len(jumplist):
    jumpval = jumplist[jump]
    jumplist[jump] = jumplist[jump] + 1
    jump = jump + jumpval
    iteration = iteration + 1
print(str(iteration))


jumplist = []
with open("day5.txt") as jumpinstructions:
    for jumpinstruction in jumpinstructions:
        jumplist.append(int(jumpinstruction))

jump = 0
iteration = 0
while jump < len(jumplist):
    jumpval = jumplist[jump]
    if jumpval >= 3:
        jumplist[jump] = jumplist[jump] - 1
    else:
        jumplist[jump] = jumplist[jump] + 1
    jump = jump + jumpval
    iteration = iteration + 1
print(str(iteration))