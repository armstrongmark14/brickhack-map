"""This is the driver for my program. Here is where
to run the code for generating a graph of nodes over a map.

Then you can find an intersection and trace a path from point
to point using the nodes.
"""

from classes import NodeFileReader
from classes import NodeFinder
from classes import SearchTreeGenerator as ST
from classes import TreeTraverser
from classes import UserInputHandler

# Getting all the user input nicely
uih = UserInputHandler.UserInputHandler()

# Asking for a map file to use
uih.mapPrompt()

# Getting two pairs of GPS coordinates from the user
uih.GPSCoordinatePrompt()
uih.GPSCoordinatePrompt()

# Starting the timer to time program execution
uih.startTimer()

# Making an intersection finder object to pas into NodeFileReader
nodeFinder = NodeFinder.NodeFinder(uih.getCoordinates())

# Getting the nodes from the node file (Comment the two below if running from .osm)
nodeReader = NodeFileReader.NodeFileReader(nodeFinder, uih.getMap() + '.txt')
nodeReader.read()

# Pass the nodes along with start and end points to the search tree generator
searchTree = ST.SearchTreeGenerator(nodeReader.getNodes(), nodeFinder.getSearchValues())

# If search doesn't find a path it will exit the program
# This one searches for the path with the fewest nodes -> BFS
# searchTree.searchFewestNodes()
# This one searches for the path with the shortest point-point distance -> Dijkstra's
searchTree.searchShortestPath()

# Search found a path, so time to traverse it and produce an output path
tt = TreeTraverser.TreeTraverser(nodeReader.getNodes(), nodeFinder.getEnd(), uih.getMap())
tt.traverse()

# Outputing the total time the program takes.
uih.outputTimeTaken()
uih.compareToGoogleLink()
