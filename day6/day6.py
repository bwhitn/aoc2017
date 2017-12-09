import copy
import re
import math

with open("day6.txt") as reg:
    regtextvalues = re.split("\s+", reg.read())
regvalues = []
for textvalue in regtextvalues:
    if textvalue.isdecimal():
        regvalues.append(int(textvalue))

listoflist = set()

def get_high_index(thelist):
    high = 0
    for index in range(0, len(thelist)):
        if thelist[high] < thelist[index]:
            high = index
    return high

def redestribute_values(list_values, value, start_index):
    loop = True
    while loop:
        for index in range(0 + start_index, len(list_values)):
            if value > 0:
                list_values[index] = list_values[index] + 1
                value = value - 1
            else:
                loop = False
                break
        start_index = 0
    return

def list_has_match(current_list, list_of_list):
    test_val = prep_for_set(current_list)
    if test_val in list_of_list:
        return True
    return False

def prep_for_set(current_list):
    tmp_list = []
    for val in current_list:
        tmp_list.append(chr(val + 0x20))
    return ''.join(tmp_list)

iteration = 0
iteriter = 0
while iteriter < 2:
    iteration = 0
    while not list_has_match(regvalues, listoflist):
        highindex = get_high_index(regvalues)
        highvalue = int(regvalues[highindex])
        listoflist.add(prep_for_set(copy.deepcopy(regvalues)))
        regvalues[highindex] = 0
        start_index = (highindex + 1) % len(regvalues)
        redestribute_values(regvalues, int(highvalue), start_index)
        iteration = iteration + 1
    iteriter = iteriter + 1
    print("The {0} loop iteration is {1}".format(str(iteriter), str(iteration)))
    listoflist = set()
