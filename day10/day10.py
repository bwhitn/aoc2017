__author__ = 'brianwhitney'

#listofvalues = [192, 69, 168, 160, 78, 1, 166, 28, 0, 83, 198, 2, 254, 255, 41, 12]
listofvalues = []
with open("/Users/brianwhitney/PycharmProjects/aoc2017/day10/day10.txt") as values:
    for char in values.read().strip():
        listofvalues.append(ord(char))
#listofvalues = []
listofvalues = listofvalues + [17, 31, 73, 47, 23]
rounds = 64
size = 256
#size = 5
#listofvalues = [3, 4, 1, 5]
loc = 0

skip_size = 0
thelist = range(0, size)

def get_reverse_slice(loc, length, num_list):
    if loc + length > len(num_list):
        vals = thelist[loc:size]
        vals = vals + thelist[0:length - len(vals)]
    else:
        vals = thelist[loc: loc + length] #may need to add skip and handle large list
    return vals[::-1]

while rounds > 0:
    for length in listofvalues:
        loc = (loc + skip_size) % size
        count = loc
        vals = get_reverse_slice(loc, length, thelist)
        for item in vals:
            thelist[count] = item
            count = count + 1
            if count >= size:
                count = 0
        loc = loc + length - 1
        skip_size = skip_size + 1
    rounds = rounds - 1

#print "First two multiplied: {}".format(thelist[0] * thelist[1])

hash = ""
dense_set = 0
while dense_set < 256:
    piece = thelist[dense_set:dense_set+16]
    piece_value = 0
    for item in piece:
        piece_value = piece_value ^ item
    hash = hash + "%0.2X" % piece_value
    dense_set = dense_set + 16
print hash.lower()