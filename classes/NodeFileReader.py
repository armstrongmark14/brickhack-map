"""This class will read in nodes from our special node file 
and store. It will also provide easy access to the nodes
for later.
"""

from classes import Node

class NodeFileReader():
    """This class will hold the graphs/filename and when called will 
    read the entire file to create a dictionary of nodes that we can use.
    """

    def __init__(self, intersectionFinder, nodeFilename):
        """Takes in a filename of a node file from the graphs/ folder.
        
        :param self: This.
        :param nodeFilename: Filename of our special node file
        """   
        self.intersectionFinder = intersectionFinder
        self.filename = nodeFilename
        self.nodes = dict()

    def read(self):
        """Reads the file and creates a dictionary of nodes, adding one
        every 4 lines. Pretty simple loop through every 4 lines of node
        data.
        """   
        file = open('graphs/' + self.filename, 'r')
        # Setting up variables to store things while we iterate
        i = 0
        nodeId = 0
        lat = 0
        lon = 0
        nodes = []

        for line in file:
            # Node ID #
            if i % 4 == 0:
                nodeId = line.strip()
            
            # Node GPS Coordinates
            elif i % 4 == 1:
                lat = line.split()[0]
                lon = line.split()[1]

            # List of adjacent nodes
            elif i % 4 == 2:
                nodes = line.split()
                # Have to remove whitespace in case not findable
                for n in nodes:
                    n = n.strip()

            # Last line of the node = create node
            else:
                self.nodes[nodeId] = Node.Node(nodeId, lat, lon)
                self.nodes[nodeId].setAdjacent(nodes)
                # Streets aren't in a variable
                streets = line.split('\"')
                streets.pop(0)
                streets.pop(len(streets) - 1)
                # Removing " " strings from the results
                while len(streets) % 2 == 1:
                    streets.pop(len(streets) - 2)
                self.nodes[nodeId].setStreets(streets)

                # Testing to see if this node is the closest to either
                # of our start/end points
                self.intersectionFinder.compareCoordinates(self.nodes[nodeId])

            # Increment the line counter
            i += 1

    def getNodes(self):
        """Will return the entire dictionary of nodes."""   
        return self.nodes

    def getNode(self, nodeID):
        """Will get a node reference by it's ID #.

        :param self: This.
        :param nodeID: The node ID that we want to retrieve the node of.
        """   
        return self.nodes[nodeID]
    