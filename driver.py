"""This is the driver for my program. Here is where
to run the code for generating a graph of nodes over a map.

Then you can find an intersection and trace a path from point
to point using the nodes.
"""

from classes import NodeFileReader
from classes import IntersectionFinder
from classes import SearchTreeGenerator as ST
from classes import TreeTraverser
from classes import UserInputHandler

# Getting all the user input nicely
uih = UserInputHandler.UserInputHandler()

# Asking for a map file to use
uih.mapPrompt()

# Getting the intersections from the user
uih.streetPrompt()
uih.streetPrompt()
uih.streetPrompt()
uih.streetPrompt()

# beagle ashford
# malcolm cartagena

# Starting the timer to time program execution
uih.startTimer()

# NOTE
#
# Follow this if you want to go straight from
# the .osm file without converting to my node format beforehand.
# 
# This will take significantly longer on each run. I designed it so
# that you only have to perform the slowest operation once.
#
# To do that, uncomment these three lines and comment 
# out the lower two nodeReader lines from classes import GraphGen
# nodeReader = GraphGen.GraphGen(uih.getMap())
# nodeReader.createGraph()

# Getting the nodes from the node file
nodeReader = NodeFileReader.NodeFileReader(uih.getMap() + '.txt')
nodeReader.read()

# Searching for the user's intersetions.
# These will error out if an intersection isn't found.
inter = IntersectionFinder.IntersectionFinder()
inter.find(nodeReader.getNodes(), uih.getStreet(0), uih.getStreet(1))
inter.find(nodeReader.getNodes(), uih.getStreet(2), uih.getStreet(3))

# Pass the nodes along with start and end points to the search tree generator
searchTree = ST.SearchTreeGenerator(nodeReader.getNodes(), inter.getStart(), inter.getEnd())
# If search doesn't find a path it will exit the program
searchTree.search()

# Search found a path, so time to traverse it and produce an output path
tt = TreeTraverser.TreeTraverser(nodeReader.getNodes(), inter.getEnd(), uih.getMap())
tt.traverse()

# This just outputs the intersections again so you can see them easier
# if you want to repeat
uih.outputIntersections()

# Outputing the total time the program takes.
uih.outputTimeTaken()
