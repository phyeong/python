# numSuccesses = 100
# numFailures = 0
# # successFailureRatio = numSuccesses/float(numFailures)
# # print("The success/failure ratio is", successFailureRatio)
# # print("Now here")
# try:
#     successFailureRatio = numSuccesses/float(numFailures)
#     print("The success/failure ratio is", successFailureRatio)
# except:
#     print('No failures, so the success/failure ratio is undefined.')
# print('Now here')

# def sumDigits(s):
#     """ Assumes s is a string
#         Returns the sum of the decimal digits in s
#             For example, if s is 'a2b3c' it returns 5 """
#     sum = 0
#     for i in s:
#         try:
#             sum += int(i)
#         except ValueError:
#             continue
#     print(sum)
#     return sum
# sumDigits('a2b3c')

# # # # val = int(input('Enter an integer :'))
# # # # print('The square of the number you entered is ', val**2)
# # # while True:
# # #     val = input('Enter an integer :')
# # #     try:
# # #         val = int(val)
# # #         print('The square of the number you entered is ', val**2)
# # #         break
# # #     except ValueError:
# # #         print(val, 'is not an integer.')
# # def readInt():
# #     while True:
# #         val = input('Enter an integer :')
# #         try:
# #             return(int(val))
# #         except:
# #             print(val, 'is not an integer.')
# # val = readInt()
# # print('The square of the number you entered is ', val**2)
# def readValue(valType, requestMsg, errorMsg):
#     while True:
#         val = input(requestMsg +' :')
#         try:
#             return(valType(val))
#         except:
#             print(val, errorMsg)
# val = readValue(int, 'Enter an integer', 'is not an integer')
# print('The square of the number you entered is ', val**2)

# def findAnEven(L):
#     """ Assumes L is a list of integers
#         Returns the first even number in L
#         Raise ValueError if L does not contain an even number """
#     for e in L:
#         for e in L:
#             if e%2 == 0:
#                 return e
#         raise ValueError(L, ' does not contain an even number')
# try:
#     print(findAnEven([2]))
#     print(findAnEven([1, 3, 5]))
#     print(findAnEven([1, 3, 4]))
# except ValueError as msg:
#     print(msg)

# # def getRatios(vect1, vect2):
# #     """ Assumes vect1 and vect2 are equal length lists of numbers
# #         Returns a list containing the meaningful values of vect1[i]/vect2[i] """
# #     ratios = []
# #     for index in range(len(vect1)):
# #         try:
# #             ratios.append(vect1[index] / vect2[index])
# #         except ZeroDivisionError:
# #             ratios.append(float('nan'))
# #         except:
# #             raise ValueError('getRatios called with bad arguemnts')
# #     return ratios
# # try:
# #     print(getRatios([1.0, 2.0, 7.0, 6.0], [1.0, 2.0, 0.0, 3.0]))
# #     print(getRatios([], []))
# #     print(getRatios([1.0, 2.0], [3.0]))
# #     print(getRatios([1.0, 2.0, 7.0, 6.0], [1.0, 2.0, 3.0, 4.0]))
# # except ValueError as msg:
# #     print(msg)
# def getRatios(vect1, vect2):
#     ratios = []
#     if len(vect1) != len(vect2):
#         raise ValueError('getRatios called with bad arguments')
#     for index in range(len(vect1)):
#         vect1Elem = vect1[index]
#         vect2Elem = vect2[index]
#         if (type(vect1Elem) not in (int, float)) or (type(vect2Elem) not in (int, float)):
#             raise ValueError('getRatios called with bad arguments')
#         if vect2Elem == 0.0:
#             ratios.append(float('nan'))
#         else:
#             ratios.append(vect1Elem/vect2Elem)
#     return ratios
# try:
#     print(getRatios([1.0, 2.0, 7.0, 6.0], [1.0, 2.0, 0.0, 3.0]))
#     print(getRatios([], []))
#     print(getRatios([1.0, 2.0], [3.0]))
#     print(getRatios([1.0, 2.0, 7.0, 6.0], [1.0, 2.0, 3.0, 4.0]))
# except ValueError as msg:
#     print(msg)

# def getGrades(fname):
#     try:
#         gradeFile = open(fname, 'r')
#     except IOError:
#         raise ValueError('getGrades could not open ' + fname)
#     grades = []
#     for line in gradeFile:
#         try:
#             grades.append(float(line))
#         except:
#             raise ValueError('Unable to covert line to float')
#     return grades
# try:
#     grades = getGrades('quiz1grades.txt')
#     grades.sort()
#     median = grades[len(grades)//2]
#     print('Median grade is', median)
# except ValueError as errorMsg:
#     print('Whoops.', errorMsg)
