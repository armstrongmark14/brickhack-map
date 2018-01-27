"""This class will take in the nodes and work
to find two intersections. Then it stores those
node ID's for use in the path finder.
"""

import sys
from classes import NodeFileReader as NFR
from classes import Node

class IntersectionFinder():
    """This class works to find two points
    from 2 sets of street names. It uses regex on
    the street names.
    """

    def __init__(self):
        """Constructof for IntersectionFinder."""
        self.found = []

    def find(self, nodes, first, second):
        """Finds the intersection of these 2 streets.
        Or quits the program with an error.
        
        :param self: This.
        :param nodes: The dictionary of nodes to search.
        :param first: First street name.
        :param second: Second street name.
        """
        for key in nodes.keys():
            if nodes[key].matchIntersection(first, second):
                self.found.append(key)
                nodes[key].printNode()
                return
        # If it gets here, intersection not found.
        print('Intersection not found:')
        print(first + ' ' + second)
    
    def getStart(self):
        """Return the ID of the first point searched for."""
        return self.found[0]

    def getEnd(self):
        """Return the ID of the second point searched for."""
        return self.found[1]
            


