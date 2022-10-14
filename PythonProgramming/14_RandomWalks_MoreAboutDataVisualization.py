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

# simAll((UsualDrunk, ColdDrunk, EWDrunk), (100, 1000), 10)

class styleIterator(object):
    def __init__(self, styles):
        self.index = 0
        self.styles = styles
    def nextStyle(self):
        result = self.styles[self.index]
        if self.index == len(self.styles) - 1:
            self.index = 0
        else:
            self.index += 1
        return result

def simDrunk(numTrials, dClass, walkLengths):
    meanDistances = []
    for numSteps in walkLengths:
        print('Starting simulation of', numSteps, 'steps')
        trials = simWalks(numSteps, numTrials, dClass)
        mean = sum(trials) / len(trials)
        meanDistances.append(mean)
    return meanDistances

import pylab
def simAll1(drunkKinds, walkLengths, numTrials):
    styleChoice = styleIterator(('m-', 'r:', 'k-.'))
    for dClass in drunkKinds:
        curStyle = styleChoice.nextStyle()
        print('Starting simulation of', dClass.__name__)
        means = simDrunk(numTrials, dClass, walkLengths)
        pylab.plot(walkLengths, means, curStyle, label = dClass.__name__)
    pylab.title('Mean Distance from Origin (' + str(numTrials) + ' trials)')
    pylab.xlabel('Number of Steps')
    pylab.legend(loc = 'best')
    pylab.semilogx()
    pylab.semilogy()
    pylab.show()

# simAll1((UsualDrunk, ColdDrunk, EWDrunk), (10, 100, 1000, 10000, 100000), 100)

def getFinalLocs(numSteps, numTrials, dClass):
    locs = []
    d = dClass()
    for t in range(numTrials):
        f = Field()
        f.addDrunk(d, Location(0, 0))
        for s in range(numSteps):
            f.moveDrunk(d)
        locs.append(f.getLoc(d))
    return locs

def plotLocs(drunkKinds, numSteps, numTrials):
    styleChoice = styleIterator(('k+', 'r^', 'mo'))
    for dClass in drunkKinds:
        locs = getFinalLocs(numSteps, numTrials, dClass)
        xVals, yVals = [], []
        for loc in locs:
            xVals.append(loc.getX())
            yVals.append(loc.getY())
        meanX = sum(xVals) / len(xVals)
        meanY = sum(yVals) / len(yVals)
        curStyle = styleChoice.nextStyle()
        pylab.plot(xVals, yVals, curStyle, label = dClass.__name__ + ' mean loc. =<' + str(meanX) + ',' + str(meanY) + '>')
    pylab.title('Location at End of Walks (' + str(numSteps) + ' steps)')
    pylab.xlabel('Steps East/West of Origin')
    pylab.ylabel('Steps North/South of Origin')
    pylab.legend(loc = 'lower left')
    pylab.show()

# plotLocs((UsualDrunk, ColdDrunk, EWDrunk), 100, 200)

def traceWalk(drunkKinds, numSteps):
    styleChoice = styleIterator(('k+', 'r^', 'mo'))
    f = Field()
    for dClass in drunkKinds:
        d = dClass()
        f.addDrunk(d, Location(0, 0))
        locs = []
        for s in range(numSteps):
            f.moveDrunk(d)
            locs.append(f.getLoc(d))
        xVals, yVals = [], []
        for loc in locs:
            xVals.append(loc.getX())
            yVals.append(loc.getY())
        curStyle = styleChoice.nextStyle()
        pylab.plot(xVals, yVals, curStyle, label = dClass.__name__)
    pylab.title('Spots Visited on Walk (' + str(numSteps) + ' steps)')
    pylab.xlabel('Steps East/West of Orgin')
    pylab.ylabel('Steps North/South of Origin')
    pylab.legend(loc = 'best')
    pylab.show()

traceWalk((UsualDrunk, ColdDrunk, EWDrunk), 200)
