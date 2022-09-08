# # Page 107
# def isPal(x):
#     """ Assumes x is a list
#         Returns True  if the list is a palindrome;
#                 False otherwise """
#     temp = x
#     temp.reverse
#     if temp == x:
#         return True
#     else:
#         return False
# def silly(n):
#     """ Assumes n is an int > 0
#         Gets n inputs form user
#         Prints 'Yes' if the sequence of inputs forms a plaindrome
#                'No'  otherwise """
#     for i in range(n):
#         result = []
#         elem = input('Enter element: ')
#         result.append(elem)
#     if isPal(result):
#         print('Yes')
#     else:
#         print('No')
# silly(2)

# Page 107 ~ 109
def isPal(x):
    """ Assumes x is a list
        Returns True  if the list is a palindrome;
                False otherwise """
    temp = x[:]
    print('line 33 x, temp :', x, temp)
    temp.reverse()
    print('line 35 x, temp :', x, temp)
    if temp == x:
        return True
    else:
        return False
def silly(n):
    """ Assumes n is an int > 0
        Gets n inputs form user
        Prints 'Yes' if the sequence of inputs forms a plaindrome
               'No'  otherwise """
    result = []
    for i in range(n):
        elem = input('Enter element: ')
        result.append(elem)
    print('line 48 result :', result)
    if isPal(result):
        print('Yes')
    else:
        print('No')
silly(2)