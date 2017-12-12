__author__ = 'brianwhitney'
import re


class ElementRef:
    def __init__(self):
        self.elements = {}

    def get_element_by_name(self, name):
        return self.elements[name]

    def add_element_by_str(self, element_str):
        assert isinstance(element_str, str)
        elementlist = element_str.strip().split(" <-> ")
        self.elements[elementlist[0]] = Element(elementlist[0],elementlist[1].split(", "))

    def get_ref_of_refs(self, name):
        tmpSet = set(self.elements[name].get_refs())
        retSet = set(self.elements[name].get_refs())
        while len(tmpSet) > 0:
            tmptmpSet = set()
            for ref in tmpSet:
                for r in self.elements[ref].get_refs():
                    if r not in retSet:
                        retSet.add(r)
                        tmptmpSet.add(r)
            tmpSet = tmptmpSet
        return retSet

    def pop(self):
        return self.elements.popitem()[0]

class Element:
    def __init__(self, name, reflist):
        self.refs = set(reflist)
        self.name = name

    def get_refs(self):
        return self.refs

    def get_name(self):
        return self.name

    def __str__(self):
        retVal = self.name + ": "
        retVal = retVal + ", ".join(self.refs)
        return retVal

ref = ElementRef()
with open("day12.txt") as pipefile:
    for pipe in pipefile:
        ref.add_element_by_str(pipe)
zeroprogs = ref.get_ref_of_refs("0")
print "The number of programs connected to program zero: {}".format(len(zeroprogs))
setval = set()
for i in range(0, 2000):
    setval.add(str(i))
count = 1
setval = setval - zeroprogs
while len(setval) > 0:
    elem = setval.pop()
    nextset = ref.get_ref_of_refs(elem)
    setval = setval - nextset
    count = count + 1
print "The number of unique groups in the programs: {}".format(count)