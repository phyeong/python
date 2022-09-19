def search(L, e):
    """ Assumes L is a list, the elements of which are in ascending order.
        Returns True if e is in L ans
                False otherwise """
    def bSearch(L, e, low, high):
        if low == high:
            return L[low] == e
        mid = (low + high) // 2
        if L[mid] == e:
            return True
        if L[mid] > e:
            if low == mid:
                return False
            else:
                return bSearch(L, e, low, mid-1)
        else:
            return bSearch(L, e, mid+1, high)
    
    if len(L) == 0:
        return False
    else:
        return bSearch(L, e, 0, len(L)-1)

def testBSearch():
    L = [3, 5, 7, 9, 11]
    for i in [1, 4, 7, 8, 11, 13]:
        print(search(L, i))

testBSearch()
