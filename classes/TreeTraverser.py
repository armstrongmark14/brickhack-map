"""TreeTraverser is a class that will take in the end point
of a tree and traverse back to the start.
"""

from classes import Node

class TreeTraverser():
    """This class simply takes the nodes and the end point
    of the tree and traverses back to the start while outputing
    the GPS coordinates of each node to a file in outputs/.
    """

    def __init__(self, nodes, start, filename):
        """Constructor taking in all that the tree traverser needs.
        
        Note: It still needs a reference to the nodes dictionary
        because the node.parent in each node is only the ID of 
        the parent node and not a reference to it.
        
        :param self: This.
        :param nodes: The nodes that this will run over sinc
        :param start: The start point of the traversal back to the end.
        :param filename: The filename of the file that will be in outputs/
        """   
        self.nodes = nodes
        self.start = start
        self.filename = filename

    def traverse(self):
        """Will traverse back to the original node and print all of the 
        GPS coordinates into a file in outputs/ so they can be mapped.

        Use https://www.darrinward.com/lat-long/ to map th eGPS coordinates
        and get a nice looking path from start to end.
        """
        file = open('output/' + self.filename + '.txt', 'w')
        current = self.start
        while current != None:
            file.write(self.nodes[current].getCoordinates())
            current = self.nodes[current].getParent()

        file.close()
        
    
