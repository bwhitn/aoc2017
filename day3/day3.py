__author__ = 'brianwhitney'

import math

thepoint = 277678
size = pointone = 0
thepoint_sqrt = math.sqrt(thepoint)

# Size of the box
size = int(thepoint_sqrt)
if float(int(thepoint_sqrt)) != thepoint_sqrt:
    size = size + 1
print "size is: {}".format(str(size))

# Find point 1
pointone = size / 2
if size % 2 != 1:
    pointone = pointone - 1
print "Point one is at: {0}, {0}".format(str(pointone))

# Find out where it is on the outside of the box
outersteps_x = outersteps_y = 0
outersteps_frommax = thepoint - (size - 1)**2 + 1
outersteps_sides = float(outersteps_frommax) / float(size)
if int(outersteps_sides) == 0:
    outersteps_x = size - 1
    outersteps_y = size - outersteps_frommax
elif int(outersteps_sides) == 1:
    outersteps_y = 0
    outersteps_x = size * 2 - outersteps_frommax
elif int(outersteps_sides) == 2:
    outersteps_x = 0
    outersteps_y = size * 2 - outersteps_frommax
elif int(outersteps_sides) == 3:
    outersteps_y = size - 1
    outersteps_x = size * 3 - outersteps_frommax


print "Location of point is {0}, {1}".format(outersteps_x, outersteps_y)

dist = abs(pointone - outersteps_x) + abs(pointone - outersteps_y)

print "The distance is : {}".format(dist)


#-------------------------

point_num = 1
matrix = [[0 for x in range(size)] for y in range(size)]
#matrix = [[0]* size] * size
start_point = (pointone, pointone)
current_point = start_point

#set the center value
matrix[current_point[0]][current_point[1]] = 1

def calc_current_box(value):
    value_sqrt = math.sqrt(value)
    tmp_size = int(value_sqrt)
    if float(int(value_sqrt)) != value_sqrt:
        tmp_size = tmp_size + 1
    if tmp_size % 2 == 0:
        tmp_size = tmp_size + 1
    return tmp_size


def move_one_with_state():
    global point_num
    point_num = point_num + 1
    box_size = calc_current_box(point_num)
    outersteps = point_num - (box_size - 2)**2
    side_size = (box_size**2 - (box_size - 2)**2) / 4
    if outersteps <= side_size:
        outersteps_x = pointone + box_size / 2
        outersteps_y = (pointone + box_size / 2) - outersteps
    elif outersteps > side_size and outersteps <= side_size * 2:
        outersteps_y = pointone - box_size / 2
        outersteps_x = (pointone + box_size / 2) - (outersteps - side_size)
    elif outersteps > side_size * 2 and outersteps <= side_size * 3:
        outersteps_x = pointone - box_size / 2
        outersteps_y = (pointone - box_size / 2) + (outersteps - side_size * 2)
    elif outersteps > side_size * 3 and outersteps <= side_size * 4:
        outersteps_y = pointone + box_size / 2
        outersteps_x = (pointone - box_size / 2)  + (outersteps - side_size * 3)
    point = (outersteps_x, outersteps_y)
    calc_and_set_point(point)
    return point

def calc_and_set_point(point):
    global matrix
    the_matrix = matrix
    sum_val = 0
    x_max = point[0] + 1
    x_min = point[0] - 1
    y_max = point[1] + 1
    y_min = point[1] - 1
    x_val = point[0]
    y_val = point[1]
    if x_min >= 0 and y_max < size:
        sum_val = sum_val + matrix[x_min][y_max]
    if x_min >= 0:
        sum_val = sum_val + matrix[x_min][y_val]
    if x_min >= 0 and y_min >= 0:
        sum_val = sum_val + matrix[x_min][y_min]
    if x_max < size and y_max < size:
        sum_val = sum_val + matrix[x_max][y_max]
    if x_max < size:
        sum_val = sum_val + matrix[x_max][y_val]
    if x_max < size and y_min >= 0:
        sum_val = sum_val + matrix[x_max][y_min]
    if y_max < size:
        sum_val = sum_val + matrix[x_val][y_max]
    if y_min >= 0:
        sum_val = sum_val + matrix[x_val][y_min]
    matrix[x_val][y_val] = sum_val
    return sum_val

for i in range(0, thepoint):
    the_current_point = move_one_with_state()
    if (matrix[the_current_point[0]][the_current_point[1]] > thepoint):
        print "Point {0}, {1} has value {2}".format(the_current_point[0], the_current_point[1], matrix[the_current_point[0]][the_current_point[1]])
        break