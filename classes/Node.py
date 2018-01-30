"""This is the basic Node class for a point on the map.

Each node will have:
    id: ID # of this node
    latitude: Latitude of this node
    longitude: Longitude of this node
    streets: Street names this node sits on
    adjacent: Node ID's of adjacent nodes
    parent: Node ID # for search tree
    checked: Whether or not this node has been seen by the search
"""

import re

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
        self.checked = False

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

    def setAdjacent(self, nodeList):
        """Setting the list of node ID #'s to the adjacent list.
    
        :param self: This.
        :param nodeList: The list of nodes that we're setting as this nodes adjacent.
        """   
        self.adjacent = nodeList

    def setStreets(self, streets):
        """Setting a list of streets to be this nodes list of streets.
        
        :param self: This. 
        :param streets: List of streets that we're setting as this nodes streets.
        """   
        self.streets = streets

    def setParent(self, parent):
        """Sets the Node's parent equal to the ID # of the parent Node
        
        :param self: This.
        :param parent: ID of the parent node.
        """   
        self.parent = parent

    def setChecked(self, val):
        """Sets whether or not the node has been checked in a search.

        :param self: This.
        :param checked: True/False whether or not node has been checked.
        """
        self.checked = val

    def wasChecked(self):
        """Gets the checked status of this node."""
        return self.checked

    def getParent(self):
        """Returns the parent of this node in the tree."""
        return self.parent

    def getAdjacent(self):
        """Returns the list of adjacent nodes."""
        return self.adjacent

    def getStreets(self):
        """Getter for all streets of this node."""
        return self.streets

    def getId(self):
        """Returns the ID # of this node."""
        return self.id

    def getGPSCoordinates(self):
        """Returns the list of GPS coordinates"""
        return [float(self.latitude), float(self.longitude)]

    def getCoordinates(self):
        """Returns the GPS coordinates of this node nicely formatted for mapping"""
        return self.latitude + ', ' + self.longitude + '\n'

    def getInfo(self):        
        """Provide the node's contents in a string format.
        
        Return Format: 
        id
        lat lon
        nodeId1 nodeId2 nodeId3
        "street1 ave" "street2 boulevard" "street3 drive"

        :param self: This.
        """
        result = self.id
        result += '\n' + self.latitude + ' ' + self.longitude + '\n'
        for node in self.adjacent:
            result += node + ' '
        result += '\n'
        for street in self.streets:
            result += '\"' + str(street) + '\" '
        result += '\n'
        return result

    def printNode(self):
        """This will print the Node's data in a pretty way.
        
        :param self: This.
        """   
        print(self.getInfo())

    def matchIntersection(self, first, second):
        """Try to match these two streets to the streets of this node.
        
        :param self: This.
        :param first: First street name.
        :param second: Second street name.
        """   
        reg1 = re.compile(first, re.IGNORECASE)
        reg2 = re.compile(second, re.IGNORECASE)
        t1 = 0
        t2 = 0
        for street in self.streets:
            if reg1.search(street):
                t1 += 1
            if reg2.search(street):
                t2 += 1
        return t1 >= 1 and t2 >= 1
