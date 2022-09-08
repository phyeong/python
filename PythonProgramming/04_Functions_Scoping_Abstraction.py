# # Page 48 Finger
# def isIn(a, b):
#     if a in b:
#         return True
#     else:
#         return False
# print(isIn('my', 'dream is lotto'))
# print(isIn('my', 'dream is my house'))

# # Page 51
# def f(x):
#     def g():
#         x = 'abc'
#         print('x =', x)
#     def h():
#         z = x
#         print('z =', z)
#     x = x + 1
#     print('x =', x)
#     h()
#     g()
#     print('x =', x)
#     return g
# x = 3
# z = f(x)
# print('x =', x)
# print('z =', z)
# z()

# # Page 54
# def findRoot(x, power, epsilon):
#     """ Assumes x and epsilon int or float, power an int,
#             epsilon > 0 & power >= 1
#         Returns float y such that y**power is within epsilon of x.
#             If such a float does not exist, it returns None"""
#     if x < 0 and power%2 == 0: # Negative number has no even-powered roots
#         return None
#     low = min(-1.0, x)
#     high = max(1.0, x)
#     ans = (high + low)/2.0
#     while abs(ans**power - x) >= epsilon:
#         if ans**power < x:
#             low = ans
#         else:
#             high = ans
#         ans = (high + low)/2.0
#     return ans
# def testFindRoot():
#     epsilon = 0.0001
#     for x in [0.25, -0.25, 2, -2, 8, -8]:
#         for power in range(1, 4):
#             print('Testing x =', x, 'and power =', power)
#             result = findRoot(x, power, epsilon)
#             if result == None:
#                 print('         No root')
#             else:
#                 print('       ', result**power, '~=', x)
# # help(findRoot)
# testFindRoot()

# # Page 59
# def factI(n):
#     """ Assumes n an int > 0
#         Returns n! """
#     result = 1
#     while n > 1:
#         result = result * n
#         n -= 1
#     return result
# def factR(n):
#     """ Assumes n an int > 0
#         Returns n! """
#     if n == 1:
#         return 1
#     else:
#         return n * factR(n-1)
# def testFactIR():
#     for i in range(1, 10, 2):
#         print('Factorial', i, ':', factI(i), factR(i))
# testFactIR()

# # Page 61
# def fib(n):
#     """ Assumes n int >+ 0
#         Returns Fibonacci of n """
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# def testFib(n):
#     for i in range(n+1):
#         print('fib of', i, '=', fib(i))
# testFib(6)

# # Page 63
# def isPalindrome(s):
#     """ Assumes s is a str
#         Returns True if letters in s form a palindrome; False otherwise.
#         Non-letters and capitalization are ignored. """
#     def toChars(s):
#         s = s.lower()
#         letters = ''
#         for c in s:
#             if c in 'abcdefghijklmnopqrstuvwxyz':
#                 letters += c
#         return letters
#     def isPal(s):
#         print('  isPal called with', s)
#         if len(s) <= 1:
#             print('   About to return True from base case')
#             return True
#         else:
#             answer = s[0] == s[-1] and isPal(s[1:-1])
#             print('   About to return', answer, 'for', s)
#             return answer
#     return isPal(toChars(s))
# def testIsPalindrome():
#     print('Try dogGod')
#     print(isPalindrome('dogGod'))
#     print('Try doGood')
#     print(isPalindrome('doGood'))
# testIsPalindrome()

# # Page 66
# def fib(x):
#     """ Assumes x an int >= 0
#         Returns Fibonacci of x """
#     global numFibCalls
#     numFibCalls += 1
#     if x == 0 or x == 1:
#         return 1
#     else:
#         return fib(x-1) + fib(x-2)
# def testFib(n):
#     for i in range(n+1):
#         global numFibCalls
#         numFibCalls = 0
#         print('fib of', i, '=', fib(i))
#         print('fib called', numFibCalls, 'times.')
# testFib(6)

# # Page 68
# import circle
# pi = 3
# print(pi)
# print(circle.pi)
# print(circle.area(3))
# print(circle.circumference(3))
# print(circle.sphereSurface(3))
# circle.pi = 3.14
# print(circle.pi)
# print(circle.area(3))

# # Page 70~72
# nameHandle = open('kids.txt', 'w')
# # for i in range(2):
# #     name = input('Enter name: ')
# #     nameHandle.write(name + '\n')
# # nameHandle.close()
# # nameHandle = open('kids.txt', 'r')
# # for line in nameHandle:
# #     print(line)
# # nameHandle.close()
# nameHandle = open('kids.txt', 'w')
# nameHandle.write('Michael\n')
# nameHandle.write('Mark\n')
# nameHandle.close()
# nameHandle = open('kids.txt', 'r')
# for line in nameHandle:
#     print(line[:-1])
# nameHandle.close()
# nameHandle = open('kids.txt', 'a')
# nameHandle.write('David\n')
# nameHandle.writelines('Andrea\n')
# nameHandle.close()
# nameHandle = open('kids.txt', 'r')
# for line in nameHandle:
#     print(line[:-1])
# nameHandle.close()
# nameHandle = open('kids.txt', 'r')
# # a = nameHandle.read()
# # print('read() :', a)
# b = nameHandle.readline()
# print('readline() :', b)
# c = nameHandle.readlines()
# print('readliens() :', c)
# nameHandle.close()
