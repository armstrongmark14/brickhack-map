"""This Edge stores distance and node ID.

This is for use in the priority queue for Dijkstra's Algorithm
to find the shortest path.
"""

import heapq

class Edge():
    """Edge class that holds current distance to the node
    along with the node ID
    """
    
    def __init__(self, distance, nodeID):
        """Constructor that takes current distance to the node passed in.
        
            :param self: This.
            :param distance: Current distance from start point to this node.
            :param nodeID: The node that is the distance from the start point.
        """  
        self.distance = distance
        self.node = nodeID

    def __lt__(self, other):
        """Comparison override for the less than < operator.
        
            :param self: This.
            :param other: The other edge object to compare to.
        """   
        return self.distance < other.distance

    def getId(self):
        """Gets the id of the node for this Edge."""
        return self.node

    def getDistance(self):
        """Gets the distance of this node from the start node."""
        return self.distance
