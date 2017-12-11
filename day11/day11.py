

with open("day11.txt") as day11:
    directions = day11.read().strip().split(",")
    #directions = "ne,ne,ne".split(",")

position = [0,0]
furthest = 0.0

def add_position(x, y):
    position[0] = position[0] + x
    position[1] = position[1] + y

for direction in directions:
    if direction == "n":
        add_position(0,1)
    elif direction == "e":
        add_position(1,0)
    elif direction == "s":
        add_position(0,-1)
    elif direction == "w":
        add_position(-1,0)
    elif direction == "ne":
        add_position(.5,.5)
    elif direction == "se":
        add_position(.5,-.5)
    elif direction == "sw":
        add_position(-.5,-.5)
    elif direction == "nw":
        add_position(-.5,.5)
    else:
        print "Bad direction \"{}\"".format(direction)
    if furthest < abs(position[0]) + abs(position[1]):
        furthest = abs(position[0]) + abs(position[1])
print "How far at the end: {}".format(abs(position[0]) + abs(position[1]))
print "Furthest ever: {}".format(furthest)