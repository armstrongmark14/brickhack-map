"""This takes in the set of nodes + 2 ID's 
and will generate a search tree on the nodes
between them so that we can iterate over them.
"""

import sys
import math
import queue                    # Only used by fewest nodes search
import heapq                    # Only used by shortest distance search
from classes import Edge

class SearchTreeGenerator():
    """This class will take the nodes and points and run BFS to
    generate a path between the nodes.
    """

    def __init__(self, nodes, start, end):
        """Takes nodes, start, end, and will set up the object 
        so that it's ready to start the search.
        
        :param self: This.
        :param nodes: The dictionary of nodes to search for a path.
        :param start: The start node for this search.
        :param end: The end node for this search.
        """   
        self.nodes = nodes
        self.start = start
        self.end = end

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
        current = self.start
        q = []
        heapq.heappush(q, Edge.Edge(1.0, current))
        # heap.put((1.0, current))    # First node has 0 distance

        # Creating a dict to check if we have seen a node previously
        unchecked = set()
        for n in self.nodes.keys():
            unchecked.add(n)
        unchecked.remove(current)

        # Simple BFS over the nodes
        while len(q) != 0:
            # Setting our current node
            current = heapq.heappop(q) # HAVE TO KEEP EDGE OBJECT
            # NEED TO KEEP ADDING DISTANCE OF PREVIOUS NODES

            # Looping through adjacent nodes
            for node in self.nodes[current.getId()].getAdjacent():
                # If the node hasn't been seen yet
                if node in unchecked:
                    # Add current as it's parent, add to queue, and mark checked
                    self.nodes[node].setParent(current.getId())
                    # This is the critical point, distance to node = distance of current + distance current to node
                    heapq.heappush(q, Edge.Edge(current.getDistance() + self.calculateDistance(current.getId(), node), node))
                    unchecked.remove(node)

                    # Checking if we have the end node
                    if node == self.end:
                        return True

        # If we exit the loop return False
        print("Could not find path between intersections.")
        sys.exit()

    def calculateDistance(self, node1, node2):
        """This gets the distance between two nodes using their GPS coordinates.
        
        :param self: This.
        :param node1: The first node.
        :param node2: The second node.
        """   n1 = self.nodes[node1].getGPSCoordinates()
        n2 = self.nodes[node2].getGPSCoordinates()
        return math.sqrt(pow(n2[0] - n1[0], 2) + pow(n2[1] - n1[1], 2))

