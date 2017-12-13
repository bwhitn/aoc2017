# noinspection PyUnresolvedReferences
import OrderedDict

class Firewall:

    def __init__(self, layersfile):
        self.layers = OrderedDict()
        self.hits = []
        self.littleMan

    def parseLayer(self, layersfile):
        with open(layersfile) as thelayers:
            for line in thelayers:
                pass

    def moveOne(self):
        pass

    def countHits(self):
        pass

    def getSeverity(self):
        pass


class Layer:

    def __init__(self, label, depth):
        self.label = label
        self.boxSize = depth
        self.loc = 0
        self.direction = "s"

    def moveOne(self):
        pass

    def isHit(self, loc):
        pass


pico = 0
