class Item(object):
    def __init__(self, name, value, weight):
        self.name = name
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight
    def __str__(self):
        result = '<' + self.name + ', ' + str(self.value) + ', ' + str(self.weight) + '>'
        return result
def value(item):
    return item.getValue()
def weightInverse(item):
    return 1.0 / item.getWeight()
def density(item):
    return item.getValue() / item.getWeight()
def greedy(items, maxWeight, keyFunction):
    """ Assumes items a list, maxWeight >= 0,
        keyFunction maps elements of items to numbers """
    copyItems = sorted(items, key=keyFunction, reverse=True)
    result = []
    totalValue, totalWeight = 0.0, 0.0
    for i in range(len(items)):
        if (totalWeight + copyItems[i].getWeight()) <= maxWeight:
            result.append(copyItems[i])
            totalValue += copyItems[i].getValue()
            totalWeight += copyItems[i].getWeight()
    return (result, totalValue)
def buildItems():
    names = ['clock', 'painting', 'radio', 'vase', 'book', 'computer']
    values = [175, 90, 20, 50, 10, 200]
    weights = [10, 9, 4, 2, 1, 20]
    Items = []
    for i in range(len(values)):
        Items.append(Item(names[i], values[i], weights[i]))
    return Items
def testGreedy(items, maxWeight, keyFunction):
    taken, val = greedy(items, maxWeight, keyFunction)
    print('Total value of items taken is', val)
    for item in taken:
        print('  ', item)
def testGreedys(maxWeight = 20):
    items = buildItems()
    print('Use greedy by value to fill knapsack of size', maxWeight)
    testGreedy(items, maxWeight, value)
    print('\nUse greedy by weight to fill knapsack of size', maxWeight)
    testGreedy(items, maxWeight, weightInverse)
    print('\nUse greedy by density to fill knapsack of size', maxWeight)
    testGreedy(items, maxWeight, density)
# testGreedys()

def getBinaryRep(n, numDigits):
    """ Assumes n and numDigits are non-negative ints
        Returns a str of length numDigits that is a binary representation of n """
    result = ''
    while n > 0:
        result = str(n%2) + result
        n = n // 2
    if len(result) > numDigits:
        raise ValueError('not enough digits')
    for i in range(numDigits - len(result)):
        result = '0' + result
    return result
def genPowerset(L):
    """ Assumes L is a list
        Returns a list of lists that contains all possible combinarions of the elements of L.
        E.g., if L is [1, 2] it will return a list wiht elements [], [1], [2], and [1, 2]. """
    powerset = []
    for i in range(0, 2**len(L)):
        binStr = getBinaryRep(i, len(L))
        subset = []
        for j in range(len(L)):
            if binStr[j] == '1':
                subset.append(L[j])
        powerset.append(subset)
    return powerset

def chooseBest(pset, maxWeight, getVal, getWeight):
    bestVal = 0.0
    bestSet = None
    for items in pset:
        itemVal = 0.0
        itemWeight = 0.0
        for item in items:
            itemVal += getVal(item)
            #itemVal += item.getValue()
            itemWeight += getWeight(item)
            #itemWeight += item.getWeight()
        if itemWeight <= maxWeight and bestVal < itemVal:
            bestVal = itemVal
            bestSet = items
    return (bestSet, bestVal)

def testBest(maxWeight = 20):
    items = buildItems()
    pset = genPowerset(items)
    taken, val = chooseBest(pset, maxWeight, Item.getValue, Item.getWeight)
    print('Total value of items taken is', val)
    for item in taken:
        print(item)

testBest()