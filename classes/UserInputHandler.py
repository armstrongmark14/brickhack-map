"""This class will handle all of the user input and provide
values to the other classes when needed.
"""

import time

class UserInputHandler():
    """This class handles taking user input so I don't clutter
    the driver.py file too much with random stuff.
    """

    def __init__(self):
        """The constructor for this object. Initializes all
        the empty variables it needs.
        """   
        self.file = ''
        self.streets = []
        self.streetPrompt
        self.startTime = 0

    def mapPrompt(self):
        """Prints out the map prompt and stores map file input."""
        self.file = input('Enter the map name (without .osm): ')

    def streetPrompt(self):
        """Prints the street prompts.
        
        It increments on it's own, so if you want to add more
        intersections, tweak the code.
        """
        intersection = len(self.streets) / 2 + 1
        street = len(self.streets) % 2 + 1
        self.streets.append(input("Enter intersection %d street %d: " %(intersection, street)))

    def getMap(self):
        """Returns the string for the map file."""
        return self.file

    def getStreet(self, streetNum):
        """Returns the street from the list you ask for.

        :param self: This.
        :param streetNum: Index of the street you want.
        """   
        return self.streets[streetNum]

    def outputIntersections(self):
        """Will print out the intersections chosen for confirmation."""
        print('Intersection 1:\n\t%s\n\t%s' % (self.streets[0], self.streets[1]))
        print('Intersection 2:\n\t%s\n\t%s' % (self.streets[2], self.streets[3]))

    def startTimer(self):
        """Starts and stores the time the program begins after input is taken."""
        self.startTime = time.time()

    def outputTimeTaken(self):
        """Uses the start time and outputs total time elapsed."""
        print('Total Time: %f seconds.' % (time.time() - self.startTime))


