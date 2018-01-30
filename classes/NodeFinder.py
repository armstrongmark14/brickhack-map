"""This class will take in the start and end coordinates
and as we search through nodes will remember the closest
node to start and end as the inputs to our Dijkstra algorithm.
"""

import sys
from classes import Node
from classes import GetGPSDistance

class NodeFinder():
    """This class works to find two points
    from 2 sets of street names. It uses regex on
    the street names.
    """

    def __init__(self, coordinates):
        """Constructof for IntersectionFinder."""
        self.found = []

        self.getDistance = GetGPSDistance.GetGPSDistance()
        # The coordinates are inverted here because search tree inverts path
        self.startPoint = Node.Node(-1, coordinates[2], coordinates[3])
        self.endPoint = Node.Node(-2, coordinates[0], coordinates[1])
        # [0] = Node ID, [1] = Distance from xPoint
        self.closestToStart = [sys.maxsize, 0]
        self.closestToEnd = [sys.maxsize, 0]
    
    def getStart(self):
        """Return the ID of the first point searched for."""
        return self.closestToStart[1]

    def getEnd(self):
        """Return the ID of the second point searched for."""
        return self.closestToEnd[1]

    def getSearchValues(self):
        """ returns the search values nicely formatted so I don't have 
        to type each parameter into one long parameter list.
        """
        return [self.getStart(), self.getEnd()]

    def compareCoordinates(self, node):
        """Compares this node's coordinates to the start and end location, 
        if this node is the closest seen it gets remembered.
        
            :param self: This.
            :param node: The node to be checked against start/end point
        """
        distStart = self.getDistance(node, self.startPoint)
        distEnd = self.getDistance(node, self.endPoint)
        if distStart < self.closestToStart[0]:
            self.closestToStart[0] = distStart
            self.closestToStart[1] = node.getId()
        if distEnd < self.closestToEnd[0]:
            self.closestToEnd[0] = distEnd
            self.closestToEnd[1] = node.getId()
            