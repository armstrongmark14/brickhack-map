"""This is the basic Node class for a point on the map.

Each node will have:
    ID #
    GPS Coordinates
    Street Names
    Adjacent Nodes
    Parent Node ID # for search tree

"""

class Node():
    """The basic Node class for our map."""

    def __init__(self, idNum, latitude, longitude):
        """The basic constructor for the Node. Adds ID, Lat, Long.

            :param self: This.
            :param idNum: The ID # of this node.
            :param latitude: The latitude of this node.
            :param longitude: The longitude of this node
        """
        self.id = idNum
        self.latitude = latitude
        self.longitude = longitude
        self.adjacent = []
        self.streets = set()
        self.parent = None

    def addAdjacent(self, nodeId):
        """Adds a node to the adjacency list of this node
        
        :param self: This.
        :param nodeId: The ID # of the node adjacent to this.
        """   
        self.adjacent.append(nodeId)

    def addStreet(self, streetName):
        """Adds a street to this node.

        :param self: This.
        :param streetName: The name of the street this node sits on. 
        """   
        self.streets.add(streetName)

    def setParent(self, parent):
        """Sets the Node's parent equal to the ID # of the parent Node
        
        :param self: This.
        :param parent: ID of the parent node.
        """   
        self.parent = parent

    def getStreets(self):
        """Getter for all streets of this node.
        
        :param self: This. 
        """
        return self.streets

    def getId(self):
        """Returns the ID # of this node
        
            :param self: This.
        """
        return self.id

    def getInfo(self):        
        """Provide the node's contents in a string format.
        
        Return Format: 
        id
        lat lon
        nodeID-1 nodeID-2 ...
        Street(s):
            Street-1
            Street-2

        :param self: This.
        """
        result = self.id
        result += '\n' + self.latitude + ' ' + self.longitude + '\n'
        for node in self.adjacent:
            result += node + ' '
        result += '\n'
        for street in self.streets:
            result += '\"' + street + '\" '
        result += '\n'
        return result

    def printNode(self):
        """This will print the Node's data in a pretty way.
        
        :param self: This.
        """   
        print(self.getInfo())
