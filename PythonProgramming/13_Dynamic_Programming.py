# def Fib(n):
#     """ Assumes n is an int >= 0
#         Returns Fibonacci of n """
#     if n == 0 or n == 1:
#         return 1
#     result = Fib(n-1) + Fib(n-2)
#     return result
# def fastFib(n, memo = {}):
#     """ Assumes n is an int >= 0; memo used only by recursive calls
#         Returns Fibonacci of n """
#     if memo == None:
#         memo = {}
#     if n == 0 or n == 1:
#         return 1
#     try:
#         return memo[n]
#     except KeyError:
#         result = fastFib(n-1, memo) + fastFib(n-2, memo)
#         memo[n] = result
#         return result
# def testFib(n):
#     print(fastFib(n))
#     print(Fib(n))
# # testFib(35)

class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.weight = w
    def getName(self):
        return self.name
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight
    def __str__(self):
        result = '<' + self.name + ', ' + str(self.value) + ', ' + str(self.weight) + '>'
        return result
# def value(item):
#     return item.getValue()
# def weightInverse(item):
#     return 1.0 / item.getWeight()
# def density(item):
#     return item.getValue() / item.getWeight()

def maxVal(toConsider, avail):
    """ Assumes toConsider a list of items, avail a weight
        Returns a tuple of the total value of a solution
        to the 0/1 knapsack problem and the items of that solution """
    if toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getWeight() > avail:
        result = maxVal(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        withVal, withToTake = maxVal(toConsider[1:], avail - nextItem.getWeight())
        withVal += nextItem.getValue()
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail)
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    return result

def smallTest():
    names = ['a', 'b', 'c', 'd']
    vals = [6, 7, 8, 9]
    weights = [3, 3, 2, 5]
    Items = []
    for i in range(len(vals)):
        Items.append(Item(names[i], vals[i], weights[i]))
    val, taken = maxVal(Items, 5)
    for item in taken:
        print(item)
    print('Total value of items taken =', val)
smallTest()