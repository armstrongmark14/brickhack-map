"""This takes in the set of nodes + 2 ID's 
and will generate a search tree on the nodes
between them so that we can iterate over them.
"""

import sys
from queue import Queue

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
        """   self.nodes = nodes
        self.start = start
        self.end = end

    def search(self):
        """This method will run the search and exit the program if it
        doesn't find a path.
        """  
        current = self.start
        q = Queue()
        q.put(current)
        i = 0

        # Creating a dict to check if we have seen a node previously
        unchecked = set()
        for n in self.nodes.keys():
            unchecked.add(n)
        unchecked.remove(current)

        # Simple BFS over the nodes
        while not q.empty():
            # Setting our current node
            current = q.get()
            print(i)

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
