"""This is the file to run on .osm map files to generate
the more usable graph format for my program.
"""

from classes import GraphGen

mapFile = input("Enter map to parse (without .osm): ")

# This creates the GraphGen object with link to the filename
gg = GraphGen.GraphGen(mapFile)
# Parsing the .osm file and storing nodes
gg.createGraph()
# Putting the nodes in my format into outputs/mapFile.txt
gg.outputNodes(mapFile)

print('Your node file is now in outputs/%s.txt' % mapFile)
print('\nThank you for using my program.')
