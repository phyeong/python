import pylab
import random
def flip(numFlips):
    """ Assumes numFlips a positive int """
    heads = 0
    for i in range(numFlips):
        if random.choice(('H', 'T')) == 'H':
            heads += 1
    return heads / numFlips
def flipSim(numFlipsPerTrial, numTrials):
    """ Assumes numFlipsPerTrial and numTrials are positive int """
    fracHeads = []
    for i in range(numTrials):
        fracHeads.append(flip(numFlipsPerTrial))
    mean = sum(fracHeads) / len(fracHeads)
    return mean
# print('Mean = ', flipSim(10, 1))
# print('Mean = ', flipSim(10, 100))
# print('Mean = ', flipSim(100, 100000))

def regressToMean(numFlips, numTrials):
    """ Get fraction of heads for each trial of numFlips """
    fracHeads = []
    for t in range(numTrials):
        fracHeads.append(flip(numFlips))
    """ Find trials with extreme results and for each the next trial """
    extremes, nextTrials = [], []
    for i in range(len(fracHeads) - 1):
        if fracHeads[i] < 0.33 or fracHeads[i] > 0.66:
            extremes.append(fracHeads[i])
            nextTrials.append(fracHeads[i+1])
    """ Plot results """
    pylab.plot(range(len(extremes)), extremes, 'ko', label = 'Extreme')
    pylab.plot(range(len(nextTrials)), nextTrials, 'k^', label = 'Next Trial')
    pylab.axhline(0.5)
    pylab.ylim(0, 1)
    pylab.xlim(-1, len(extremes)+1)
    pylab.xlabel('Extreme Examp;le and Next Trial')
    pylab.ylabel('Fraction Heads')
    pylab.title('Regression to the Mean')
    pylab.legend(loc = 'best')
    pylab.show()
# regressToMean(15, 40)

def flipPlot(minExp, maxExp):
    """ Assumes minExp and maxExp positive integers; minExp < maxExp 
        Plots results of 2**minExp to 2**maxExp coin flips """
    ratios, diffs, xAxis = [], [], []
    for exp in range(minExp, maxExp+1):
        xAxis.append(2**exp)
    for numFlips in xAxis:
        numHeads = 0
        for n in range(numFlips):
            if random.choice(('H', 'T')) == 'H':
                numHeads += 1
        numTails = numFlips - numHeads
        try:
            ratios.append(numHeads/numTails)
            diffs.append(abs(numHeads - numTails))
        except ZeroDivisionError:
            continue
    pylab.title('Difference Between Heads and Tails')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Abs(#Heads - #Tails)')
    pylab.plot(xAxis, diffs, 'k')
#    pylab.plot(xAxis, diffs, 'ko')
    pylab.figure()
    pylab.title('Heads/Tails Ratios')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('#Heads/#Tails')
    pylab.plot(xAxis, ratios, 'k')
#    pylab.plot(xAxis, ratios, 'ko')
    pylab.show()
# random.seed(0)
# flipPlot(4, 20)