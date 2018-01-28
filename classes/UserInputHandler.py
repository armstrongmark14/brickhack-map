"""This class will handle all of the user input and provide
values to the other classes when needed.
"""

import time

class UserInputHandler():

    def __init__(self):
        self.file = ''
        self.streets = []
        self.streetPrompt
        self.startTime = 0

    def mapPrompt(self):
        self.file = input('Enter the map name (without .osm): ')

    def streetPrompt(self):
        intersection = len(self.streets) / 2 + 1
        street = len(self.streets) % 2 + 1
        self.streets.append(input("Enter intersection %d street %d: " %(intersection, street)))

    def getMap(self):
        return self.file

    def getStreet(self, streetNum):
        return self.streets[streetNum]

    def outputIntersections(self):
        print('Intersection 1:\n\t%s\n\t%s' % (self.streets[0], self.streets[1]))
        print('Intersection 2:\n\t%s\n\t%s' % (self.streets[2], self.streets[3]))

    def startTimer(self):
        self.startTime = time.time()

    def outputTimeTaken(self):
        print('Total Time: %f' % (time.time() - self.startTime))


