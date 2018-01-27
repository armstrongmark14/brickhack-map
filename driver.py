"""This is the driver for my program. Here is where
to run the code for generating a graph of nodes over a map.

Then you can find an intersection and trace a path from point
to point using the nodes.
"""

from classes import NodeFileReader as NFR
from classes import IntersectionFinder as IF

nodeReader = NFR.NodeFileReader('brighton.txt')

nodeReader.read()

intersectionFinder = IF.IntersectionFinder()
intersectionFinder.find(nodeReader.getNodes(), 'highland', 'willard')
