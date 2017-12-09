import re

goodlinecount = 0
with open("day4.txt") as numfile:
    for line in numfile:
        assert type(line) == str
        wordlist = re.split("\s+", line)
        retVal = []
        goodlinecount = goodlinecount + 1
        for word in wordlist:
            word = ''.join(sorted(word)) #
            if word in retVal:
                print "Found a duplicate"
                goodlinecount = goodlinecount - 1
                break;
            else:
                retVal.append(word)
print goodlinecount