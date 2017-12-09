import re

class TreeElement:
    def __init__(self, line):
        self.parents = set()
        self.child = None
        self.parentObjects = set()
        self.__parseLine__(line)

    def __addParent__(self, parent):
        if isinstance(parent, list):
            for item in parent:
                self.parents.add(item)
        elif isinstance(parent, str):
            if "," in parent:
                parent = parent.split(", ")
                self.__addParent__(parent)
            else:
                self.parents.add(parent)

    def __addNumber__(self, number):
        if isinstance(number, int):
            self.number = number
        else:
            self.number = int(number)

    def __parseLine__(self, line):
        assert isinstance(line, str)
        line = line.strip()
        match_info = re.match("^([a-z]+) \((\d+)\)(?: -> ([,a-z\x20]+))?", line)
        try:
            groups = match_info.groups()
            self.name = match_info.group(1)
            self.__addNumber__(match_info.group(2))
            if match_info.group(3) != None:
                self.__addParent__(match_info.group(3))
        except:
            print("Error invalid match in {}".format(line))

    def addParentObject(self, element):
        self.parentObjects.add(element)

    def getValue(self):
        return int(self.number)

    def getName(self):
        return str(self.name)

    def getParentNames(self):
        return tuple(self.parents)

    def setChild(self, child):
        self.child = child

    def getChild(self):
        if self.child != None:
            return str(self.child)
        return None

    def getParentObjects(self):
        return tuple(self.parentObjects)

    def getTotalValue(self):
        val = 0
        for parent in self.getParentObjects():
            val = val + parent.getTotalValue()
        return val + self.getValue()


class TreeObject:

    def __init__(self, treefile):
        self.theTree = {}
        self.__parseTreeFile__(treefile)

    def __parseTreeFile__(self, treefile):
        with open(treefile) as mapfile:
            for line in mapfile:
                treeItem = TreeElement(line)
                self.theTree[treeItem.getName()] = treeItem
        for value in self.theTree.values():
            assert isinstance(value, TreeElement)
            for parent in value.getParentNames():
                parent = self.theTree[parent]
                assert isinstance(parent, TreeElement)
                parent.setChild(value.getName())
                value.addParentObject(parent)

    def getItemByName(self, name):
        assert isinstance(name, str)
        return self.theTree[name]

    def getChildItem(self, treeItem):
        assert isinstance(treeItem, TreeElement)
        return treeItem.getChild()

    def getRoot(self, treeItem):
        assert isinstance(treeItem, TreeElement)
        while treeItem.getChild() != None:
            treeItem = self.getItemByName(treeItem.getChild())
        return treeItem


theTree = TreeObject("day7.txt")
#First element in list that doesn't have parent elements
parent = theTree.getItemByName("oislgqy")
assert isinstance(parent, TreeElement)
root = theTree.getRoot(parent)
print("The root child is: {}".format(root.getName()))


tmpDict = {}
elemDict = {}
tmpobj = None
oddVal = 0
modeVal = 0
while True:
    for parent in root.getParentObjects():
        print("values of parent {} is {}".format(parent.getName(), parent.getTotalValue()))
        if parent.getTotalValue() not in tmpDict:
            tmpDict[parent.getTotalValue()] = 1
        else:
            tmpDict[parent.getTotalValue()] = tmpDict[parent.getTotalValue()] + 1
        elemDict[parent.getTotalValue()] = parent
    if len(tmpDict.items()) == 1:
        break
    oddVal = 0
    modeVal = 0
    for key, value in tmpDict.items():
        if value == 1:
            oddVal = key
        else:
            modeVal = key
    tmpobj = elemDict[oddVal]
    root = tmpobj
    tmpDict = {}

print("The value of {} is {} and needs to be: {}".format(tmpobj.getName(), tmpobj.getValue(), str(tmpobj.getValue() + (modeVal - oddVal))))