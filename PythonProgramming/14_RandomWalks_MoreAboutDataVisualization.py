class Location(object):
    def __init__(self, x, y):
        self.x, self.y = x, y
    def move(self, deltaX, deltaY):
        return Location(self.x + deltaX, self.y + deltaY)
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def distFrom(self, other):
        ox, oy = other.x, other.y
        xDist, yDist = self.x - ox, self.y - oy
        return (xDist**2 + yDist**2) ** 0.5
    def __str__(self):
        return '<' + str(self.x) + ',' + str(self.y) + '>'

import random
class Drunk(object):
    def __init__(self, name = None):
        self.name = name
    def __str__(self):
        if self != None:
            return self.name
        return 'Anonymous'
class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0,1), (0,-1), (1,0), (-1,0)]
        return random.choice(stepChoices)

class Field(object):
    def __init__(self):
        self.drunks = {}
    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc
    def moveDrunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep()
        currentLocation = self.drunks[drunk]
        self.drunks[drunk] = currentLocation.move(xDist, yDist)
    def getLoc(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]

def walk(f, d, numSteps):
    """ Assumes : f a Field, d a Drunk in f, and numSteps an int >= 0.
        Moves d numSteps times.
        Returns the distance between the final location and the location at the start of the walk."""
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return start.distFrom(f.getLoc(d))

def simWalks(numSteps, numTrials, dClass):
    """ Assumes numSteps an int >= 0, numTrials an int > 0, dClass a subClass of Drunk
        Simulates numTrials walks of n9mSteps steps each.
        Returns a list of the final distances for each trial. """
    Homer = dClass()
    origin = Location(0, 0)
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(Homer, origin)
#        distances.append(round(walk(f, Homer, numTrials), 1))
        distances.append(round(walk(f, Homer, numSteps), 1))
    return distances

def drunkTest(walkLengths, numTrials, dClass):
    """ Assumes walkLengths a sequence of ints >= 0, numTrials an int > 0, dClass a subClass of Drunk
        For each number of steps in walklengths, runs simWalks with numTrials walks and prints results. """
    for numSteps in walkLengths:
        distances = simWalks(numSteps, numTrials, dClass)
        print(dClass.__name__, 'random walk of', numSteps, 'steps')
        print('Mean =', round(sum(distances)/len(distances), 4))
        print('Max =', max(distances), 'Min =', min(distances))

# drunkTest((0,1, 10, 100, 1000, 10000), 100, UsualDrunk)

class ColdDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0,1), (0,-2), (1,0), (-1,0)]
        return random.choice(stepChoices)

class EWDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(1,0), (-1,0)]
        return random.choice(stepChoices)

def simAll(drunkKinds, walkLengths, numTrials):
    for dClass in drunkKinds:
        drunkTest(walkLengths, numTrials, dClass)

simAll((UsualDrunk, ColdDrunk, EWDrunk), (100, 1000), 10)
