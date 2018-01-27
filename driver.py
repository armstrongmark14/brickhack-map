"""This is the driver for my program. Here is where
to run the code for generating a graph of nodes over a map.

Then you can find an intersection and trace a path from point
to point using the nodes.
"""

from classes import NodeFileReader as NFR
from classes import IntersectionFinder as IF
from classes import SearchTreeGenerator as ST

# Getting the nodes from the node file
nodeReader = NFR.NodeFileReader('san_diego.txt')
nodeReader.read()

# Searching for the user's intersetions.
# These will error out if an intersection isn't found.
inter = IF.IntersectionFinder()
inter.find(nodeReader.getNodes(), 'merida court', 'castejon')
inter.find(nodeReader.getNodes(), 'playa', 'yosemite')

# Pass the nodes along with start and end points to the search tree generator
searchTree = ST.SearchTreeGenerator(nodeReader.getNodes(), inter.getStart(), inter.getEnd())
# If search doesn't find a path it will exit the program
searchTree.search()

# Search found a path, so time to traverse it and produce an output path

