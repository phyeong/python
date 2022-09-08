# # Page 29
# # Find the cube root of a perfect cube using Exhaustive Enumeration
# x = int(input("Enter an integer: "))
# ans = 0
# while ans**3 < abs(x):
#     ans = ans + 1
# if ans**3 != abs(x):
#     print(x, 'is not a perfect cube')
# else:
#     if x < 0:
#         ans = -ans
#     print('Cube root of', x, 'is', ans)

# # Page 31
# # computing power test
# maxVal = int(input('Enter a positive integer: '))
# i = 0
# while i < maxVal:
#     i = i + 1
# print(i)

# # Page 31 Finger
# # input one int type from user, print the root and pwr according to the value
# x = int(input('Enter a integer: '))
# pwr = 1
# check = False
# while pwr < 6:
#     ans = 0
#     while ans**pwr < abs(x):
#         ans += 1
#     if ans**pwr == abs(x):
#         if x < 0:
#             ans = -ans
#         print(str(x) + "'s root is " + str(ans) + ' and' + ' pwr is ', str(pwr))
#         check = True
#     pwr += 1
# if check == False:
#     print("Can not fine " + str(x) + "'s root and pwr!")

# # Page 33
# x = 4
# for i in range(0, x):
#     print(i)
#     x = 2
# x = 4
# for j in range(x):
#     for i in range(x):
#         print(i)
#         x = 2

# # Page 34
# # Find the cube root of a perfect cube using Exhaustive Enumeration
# x = int(input("Enter an integer: "))
# for ans in range(0, abs(x)+1):
#     if ans**3 >= abs(x):
#         break
# if ans**3 != abs(x):
#     print(x, 'is not a perfect cube')
# else:
#     if x < 0:
#         ans = -ans
#     print('Cube root of', x, 'is', ans)

# # Page 34 Finger
# s = '1.23, 2.4, 3.123'
# temp = ''
# total = 0
# for i in s:
#     if i == ',':
#         total += float(temp)
#         temp = ''
#     else:
#         temp += i
# total += float(temp)
# print(total)

# Page 35
# Find the approximation root using Exhaustive Enumeration
# x = float(input("Enter an integer: "))
# epsilon = 0.01
# step = epsilon**2
# numGuesses = 0
# ans = 0.0
# while abs(ans**2 - x) >= epsilon and ans <= abs(x):
#     ans += step
#     numGuesses += 1
# print('numGuesses = ', numGuesses)
# if abs(ans**2 - x) >= epsilon:
#     print('Failed on square root of', x)
# else:
#     print(ans, 'is close to square of', x)

# # Page 38
# x = float(input("Enter an integer: "))
# epsilon = 0.01
# numGuesses = 0
# low = 0.0
# high = max(1.0, x)
# ans = (high + low) / 2.0
# while abs(ans**2 - x) >= epsilon:
#     print('low =', low, 'high =', high, 'ans =', ans)
#     numGuesses += 1
#     if ans**2 < x:
#         low = ans
#     else:
#         high = ans
#     ans = (high + low) / 2.0
# print('numGuesses =', numGuesses)
# print(ans, 'is close to square root of', x)

# # Page 39 Finger
# x = float(input("Enter an integer: "))
# original_x = x
# if x < 0:
#     x = -x
# epsilon = 0.01
# numGuesses = 0
# low = 0.0
# high = max(1.0, x)
# ans = (high + low) / 2.0
# while abs(ans**3 - x) >= epsilon:
#     print('low =', low, 'high =', high, 'ans =', ans)
#     numGuesses += 1
#     if ans**3 < x:
#         low = ans
#     else:
#         high = ans
#     ans = (high + low) / 2.0
# print('numGuesses =', numGuesses)
# if original_x < 0:
#     ans = -ans
# print(ans, 'is close to square root of', original_x)

# # Page 43
# # Netwon-Raphson for square root
# # Find x such that x**2 - 24 is within epsilon of 0
# epsilon = 0.01
# k = 24.0
# guess = k / 2.0
# while abs(guess**2 - 24) >= epsilon:
#     guess = guess - ((guess**2 - 24) / (2*guess))
# print('Square root of', k, 'is about', guess)

# # Page 43 Finger
# # Netwon-Raphson for square root
# # Find x such that x**2 - 24 is within epsilon of 0
# epsilon = 0.01
# k = 24.0
# guess = k / 2.0
# numGuesses = 0
# while abs(guess**2 - k) >= epsilon:
#     guess = guess - ((guess**2 - k) / (2*guess))
#     numGuesses += 1
# print('numGuesses =', numGuesses)
# print('Square root of', k, 'is about', guess)

# x = 24
# epsilon = 0.01
# numGuesses = 0
# low = 0.0
# high = max(1.0, x)
# ans = (high + low) / 2.0
# while abs(ans**2 - x) >= epsilon:
#     numGuesses += 1
#     if ans**2 < x:
#         low = ans
#     else:
#         high = ans
#     ans = (high + low) / 2.0
# print('Bisection numGuesses =', numGuesses)
# print(ans, 'is close to square root of', x)