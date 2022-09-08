# # page 27 Finger
# numXs = int(input("How many times should I print the letter X? "))
# toPrint = ''
# while numXs > 0:
#     toPrint += 'X'
#     numXs -= 1
# print(toPrint)

# # page 28 Finger
# import sys
# max = -(sys.maxsize+1)
# count = 0
# check = False
# while count < 10:
#     x = int(input("Enter integer: "))
#     if x%2 == 1:
#         check = True
#         if x > max:
#             max = x
#     count += 1
# if check == True:
#     print("Maximum Odd integer is ", max)
# else:
#     print("No odd number in the input value.")