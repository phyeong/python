# def search(L, e):
#     """ Assumes L is a list, the elements of which are in ascending order.
#         Returns True if e is in L ans
#                 False otherwise """
#     def bSearch(L, e, low, high):
#         if low == high:
#             return L[low] == e
#         mid = (low + high) // 2
#         if L[mid] == e:
#             return True
#         if L[mid] > e:
#             if low == mid:
#                 return False
#             else:
#                 return bSearch(L, e, low, mid-1)
#         else:
#             return bSearch(L, e, mid+1, high)
#     if len(L) == 0:
#         return False
#     else:
#         return bSearch(L, e, 0, len(L)-1)
# # def testBSearch():
# #     L = [3, 5, 7, 9, 11]
# #     for i in [1, 4, 7, 8, 11, 13]:
# #         print(search(L, i))
# # testBSearch()

# def selSort(L):
#     """ Assumes that L is an list of elements that can be compared using >.
#         Sorts L in ascending order """
#     suffixStart = 0
#     while suffixStart != len(L):
#         for i in range(suffixStart, len(L)):
#             if L[suffixStart] > L[i]:
#                 L[suffixStart], L[i] = L[i], L[suffixStart]
#         suffixStart += 1
# # L = [5, 3, 9, 1, 8, 4, 5, 3]
# # selSort(L)

# def merge(left, right, compare):
#     """ Assumes left and right are sorted lists and compare defines an ordering on the elements.
#         Returns a new sorted (by compare) list containing the same elements as (left + right) would contain. """
#     result = []
#     i, j = 0, 0
#     while i < len(left) and j < len(right):
#         if compare(left[i], right[j]):
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     while i < len(left):
#         result.append(left[i])
#         i += 1
#     while j < len(right):
#         result.append(right[j])
#         j += 1
#     return result

# def mergeSort(L, compare = lambda x, y : x < y):
#     if len(L) < 2:
#         return L[:]
#     else:
#         middle = len(L) // 2
#         left = mergeSort(L[:middle], compare)
#         right = mergeSort(L[middle:], compare)
#         return merge(left, right, compare)
# # def testMergeSort():
# #     L = [5, 3, 9, 1, 8, 4, 5, 3]
# #     print(mergeSort(L))
# # testMergeSort()

# def lastNameFirstname(name1, name2):
#     arg1 = name1.split(' ')
#     arg2 = name2.split(' ')
#     if arg1[1] != arg2[1]:
#         return arg1[1] < arg2[1]
#     else:
#         return arg1[0] < arg2[0]

# def firstNameLastname(name1, name2):
#     arg1 = name1.split(' ')
#     arg2 = name2.split(' ')
#     if arg1[0] != arg2[0]:
#         return arg1[0] < arg2[0]
#     else:
#         return arg1[1] < arg2[1]

# def testMerseSortFunction():
#     L = ['Tom Brady', 'Eric Grimson', 'Gisele Bundchen']
#     newL = mergeSort(L, lastNameFirstname)
#     print('Sorted by last name =', newL)
#     newL = mergeSort(L, firstNameLastname)
#     print('Sorted by first name =', newL)
# testMerseSortFunction()

class intDict(object):
    """ A dictionary with integer keys """
    def __init__(self, numBuckets):
        """ Create an empty dictionary """
        self.buckets = []
        self.numBuckets = numBuckets
        for i in range(numBuckets):
            self.buckets.append([])
    def addEntry(self, key, dicVal):
        """ Assumes key an int. Adds an entry. """
        hashBucket = self.buckets[key % self.numBuckets]
        for i in range(len(hashBucket)):
            if hashBucket[i][0] == key:
                hashBucket[i] = (key, dicVal)
                return
        hashBucket.append((key, dicVal))
    def getValue(self, key):
        """ Assumes key an int.
            Returns value associated with key """
        hashBucket = self.buckets[key % self.numBuckets]
        for e in hashBucket:
            if e[0] == key:
                return e[1]
        return None
    def __str__(self):
        result = '{'
        for b in self.buckets:
            for e in b:
                result = result + str(e[0]) + ':' + str(e[1]) + ','
        return result[:-1] + '}'
def testIntDict():
    import random
    D = intDict(29)
    for i in range(20):
        key = random.randint(0, 10**5)
        D.addEntry(key, i)
    print('The value of the intDict is :')
    print(D)
    print('\n', 'The buckets are:')
    for hashBucket in D.buckets:
        print(' ', hashBucket)
testIntDict()
