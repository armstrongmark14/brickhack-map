"""This is basically a functor that will calculate the
distance between two nodes.
"""

import math

class GetGPSDistance():
    
    def __call__(self, node1, node2):
        """This gets the distance between two nodes using their GPS coordinates.
        
        :param self: This.
        :param node1: The first node. Node object, not just ID.
        :param node2: The second node. Node object, not just ID.
        """   
        n1 = node1.getGPSCoordinates()
        n2 = node2.getGPSCoordinates()
        return math.sqrt(pow(n2[0] - n1[0], 2) + pow(n2[1] - n1[1], 2))