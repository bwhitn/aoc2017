from collections import OrderedDict

class Firewall:

    def __init__(self, layersfile, delay=0):
        self.layers = OrderedDict()
        self.hits = []
        self.end = 0
        self.parseLayers(layersfile)
        self.loc = 0
        self.delay = delay
        self.delayed = delay
        self.pico = 0

    def parseLayers(self, layersfile):
        with open(layersfile) as thelayers:
            assert isinstance(self.layers, OrderedDict)
            for line in thelayers:
                keyVal = line.strip().split(": ")
                self.layers[int(keyVal[0])] = Layer(int(keyVal[0]), int(keyVal[1]))
            keys = sorted(self.layers.keys())
            self.end = keys[len(keys) - 1]


    def rotateScanner(self):
        for layer in self.layers:
            self.layers[layer].moveOne()

    def moveOne(self):
        if self.delay > 0:
            self.pico = self.delay
            for i in range(0, self.delay):
                self.rotateScanner()
            self.delay = 0
        if self.isHit():
            self.hits.append(self.layers[self.loc])
        if self.loc == self.end:
            return False
        self.rotateScanner()
        self.loc = self.loc + 1
        self.pico = self.pico + 1
        return True


    def countHits(self):
        return len(self.hits)


    def getSeverity(self):
        total = 0
        for layer in self.hits:
            total = total + layer.getSeverity()
        return total

    def isHit(self):
        if self.loc in self.layers:
            if self.layers[self.loc].getLoc() == 0:
                return True
        return False


class Layer:

    def __init__(self, label, depth):
        self.boxSize = depth
        self.loc = 0
        self.direction = "s"
        self.label = label


    def moveOne(self):
        if self.direction == "s":
            if self.loc + 1 == self.boxSize:
                self.direction = "n"
                self.loc = self.loc - 1
            else:
                self.loc = self.loc + 1
        else:
            if self.loc == 0:
                self.direction = "s"
                self.loc = self.loc + 1
            else:
                self.loc = self.loc - 1


    def getLoc(self):
        return self.loc

    def getLabel(self):
        return self.label

    def getSeverity(self):
        return self.label * self.boxSize


firewall = Firewall("day13.txt")
while(firewall.moveOne()):
    pass

print firewall.pico
print firewall.getSeverity()


trycount = 1
while True:
    firewall = Firewall("day13.txt", trycount)
    while(firewall.moveOne()):
        if firewall.countHits() > 0:
            break
    if firewall.countHits() == 0:
        print trycount
        print "picos: {}".format(firewall.pico)
        break
    trycount = trycount + 1