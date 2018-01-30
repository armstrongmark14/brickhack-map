"""This takes in the set of nodes + 2 ID's 
and will generate a search tree on the nodes
between them so that we can iterate over them.
"""

import sys
import queue                    # Only used by fewest nodes search
import heapq                    # Only used by shortest distance search
from classes import Edge
from classes import GetGPSDistance

class SearchTreeGenerator():
    """This class will take the nodes and points and run BFS to
    generate a path between the nodes.
    """

    def __init__(self, nodes, pointValues):
        """Takes nodes, start, end, and will set up the object 
        so that it's ready to start the search.
        
        :param self: This.
        :param nodes: The dictionary of nodes to search for a path.
        :param start: The start node for this search.
        :param end: The end node for this search.
        """   
        self.nodes = nodes
        self.start = pointValues[0]
        self.end = pointValues[1]
        # Used for checking distance between nodes
        self.getDistance = GetGPSDistance.GetGPSDistance()

    def searchFewestNodes(self):
        """This method will run the search and exit the program if it
        doesn't find a path. It only searches for the path with the fewest nodes.
        """  
        current = self.start
        q = Queue()
        q.put(current)

        # Creating a dict to check if we have seen a node previously
        unchecked = set()
        for n in self.nodes.keys():
            unchecked.add(n)
        unchecked.remove(current)

        # Simple BFS over the nodes
        while not q.empty():
            # Setting our current node
            current = q.get()

            # Looping through adjacent nodes
            for node in self.nodes[current].getAdjacent():
                # If the node hasn't been seen yet
                if node in unchecked:
                    # Add current as it's parent, add to queue, and mark checked
                    self.nodes[node].setParent(current)
                    q.put(node)
                    unchecked.remove(node)

                    # Checking if we have the end node
                    if node == self.end:
                        return True

        # If we exit the loop return False
        print("Could not find path between intersections.")
        sys.exit()

    def searchShortestPath(self):
        """This method searches from start to end, but it uses Dijkstra's
        algorithm to find the shortest path.
        """  
        # Initializing some variables for use in the search
        current = self.start
        self.nodes[self.start].setChecked(True)
        q = []
        heapq.heappush(q, Edge.Edge(0.0, current))

        # Simple Dijkstra's algorithm for shortest path on the nodes
        while len(q) != 0:
            # Setting our current node
            c = heapq.heappop(q) # HAVE TO KEEP EDGE OBJECT
            current = self.nodes[c.getId()]
            currentDistance = c.getDistance()
            # NEED TO KEEP ADDING DISTANCE OF PREVIOUS NODES

            # Looping through adjacent nodes
            for n in current.getAdjacent():
                # If the node hasn't been seen yet
                node = self.nodes[n]

                if not node.wasChecked():
                    # Add current as it's parent, add to queue, and mark checked
                    node.setParent(current.getId())
                    # Checking if we have the end node
                    if node.getId() == self.end:
                        return True

                    # This is the critical point, distance to node = distance of current + distance current to node
                    heapq.heappush(q, Edge.Edge(currentDistance + self.getDistance(current, node), node.getId()))
                    node.setChecked(True)
                    

        # If we exit the loop return False
        print("Error: Could not find path between intersections.")
        sys.exit()

    def calculateDistance(self, node1, node2):
        """This gets the distance between two nodes using their GPS coordinates.
        
        :param self: This.
        :param node1: The first node.
        :param node2: The second node.
        """   
        n1 = self.nodes[node1].getGPSCoordinates()
        n2 = self.nodes[node2].getGPSCoordinates()
        return math.sqrt(pow(n2[0] - n1[0], 2) + pow(n2[1] - n1[1], 2))

