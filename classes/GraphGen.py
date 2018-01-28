"""This class will take in a filename to a .osm file and
then you can generate a graph using the createGraph() function.

After the graph is generated, use outputNodes('filename.txt') to 
generate a file in the outputs/ folder with the well-formated nodes
that are easier to use in the path finding functions.
"""

import xml.etree.ElementTree as ET
from classes import Node

class GraphGen():
    """This class will provide helper functions to generate the graph
    file that is much quicker to parse and use than the .osm file.
    """   

    def __init__(self, file):
        """The constructor for the GraphGen takes only a filename from
        the maps folder.
        
        :param self: This.
        :param file: Filename without maps/ and .osm
        """   
        self.root = ET.parse('maps/' + file + '.osm').getroot()
        self.nodes = dict()

    def printNodes(self):
        """This will print all the nodes to the terminal."""
        for n in self.nodes:
            self.nodes[n].printNode()

    def outputNodes(self, filename):
        """This will output the nodes to the .txt file you specify 
        in the outputs/ folder.
        
        :param self: This.
        :param filename: Filename for file generated in the outputs/ folder.
        """   
        file = open('graphs/' + filename + '.txt', 'w')
        for n in self.nodes:
            if len(self.nodes[n].getStreets()) > 0:
                file.write(self.nodes[n].getInfo())
        file.close()

    def createGraph(self):
        """This is the main fuction that generates the graph from
        the .osm file provided when constructing this object.
        """   
        for child in self.root:
            if child.tag == 'node':
                # If we have a node object throw it to the addNode() function to create it
                self.addNode(child.get('id'), child.get('lat'), child.get('lon'))

            # Making the street name a variable so we can use it twice
            street = child.find('.//tag[@k="name"]')
            highway = child.find('.//tag[@k="highway"]')
            # Checking if we have a 'way' tag && it is a 'highway' (road) && it has a street name
            if child.tag == 'way' and highway != None and highway.get('v') != 'footway' and street != None:
                self.connectWay(child, street.get('v'))
    

    
    def addNode(self, idNum, latitude, longitude):
        """Will create a node in self.nodes dictionary with the specified values.
        
        :param self: This.
        :param idNum: The ID # of the node we are creating.
        :param latitude: The latitude of the node we are creating.
        :param longitude: The longitude of the node we are creating.
        """   
        self.nodes[idNum] = Node.Node(idNum, latitude, longitude)


    def connectWay(self, way, streetName):
        """Loops through the way tag, finding 'nd' (nodes) and then connecting
        together adjacent nodes for the graph. At the end it also adds the street
        name of this street to the nodes in the street.
        
        :param self: This.
        :param way: The way tag that contains references to all of the nodes that
        are on the street.
        :param streetName: The street name of the street tag 
        """   
        prev = None                                                             
        # Now looping through the nodes of this parent way                      
        for element in way:                                                    
            if element.tag == 'nd':                                                  
                # Adding both nodes to each other's adjacency lists             
                if prev != None:                                                
                    self.connectNodes(prev.getId(), element.get('ref'))              
                prev = self.nodes[element.get('ref')]                                
                # If the street has a name, add it to the node                  
                self.nodes[element.get('ref')].addStreet(streetName)                     
            else:                                                               
                return  

    def connectNodes(self, node1, node2):
        """This will take two nodes and give them connections to each other.
        
        :param self: This.
        :param node1: Node 1 to connect to Node 2.
        :param node2: Node 2 to connect to Node 1.
        """   
        self.nodes[node1].addAdjacent(node2)
        self.nodes[node2].addAdjacent(node1)

    def getNodes(self):
        """Returns the nodes if you want to go straight from .osm to path"""
        return self.nodes