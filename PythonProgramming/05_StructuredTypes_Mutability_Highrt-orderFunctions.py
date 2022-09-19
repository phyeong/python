# # Page 75
# def intersect(t1, t2):
#     """ Assumes t1 and t2 are tuples
#         Returns a tuple containing elements that are in both t1 and t2 """
#     result = ()
#     for e in t1:
#         if e in t2:
#             result += (e,)
#     return result
# t1 = (1, 'two', 3)
# t2 = (1.0, 2.0, 3.25)
# print(intersect(t1, t2))

# # Page 75
# def findExtremeDivisors(n1, n2):
#     """ Assumes that n1 and n2 are positive ints
#         Returns a tuple containing the smallest common divisor > 1 and the largest common divisior of n1 and n2.
#         If no common divisor, other than 1, returns (None, None) """
#     minVal, maxVal, = None, None
#     for i in range(2, min(n1, n2) + 1):
#         if n1%i == 0 and n2%i == 0:
#             if minVal == None:
#                 minVal = i
#             maxVal = i
#     return(minVal, maxVal)
# a, b = findExtremeDivisors(210, 740)
# print(a, b)

# # Page 77 ~ 79
# Techs = ['MIT', 'Caltech']
# Ivys = ['Harvard', 'Yale', 'Brown']
# Univs1 = [Techs, Ivys]
# Univs2 = [['MIT', 'Caltech'], ['Harvard', 'Yale', 'Brown']]
# print('Univs1 =', Univs1)
# print('Univs2 =', Univs2)
# print(Univs1 == Univs2)          # test value equality
# print(id(Univs1) == id(Univs2))  # test object equality
# print('Id of Univs1 =', id(Univs1))
# print('Id of Univs2 =', id(Univs2))
# print('Ids of Univs1[0] and Univs1[1]', id(Univs1[0]), id(Univs1[1]))
# print('Ids of Univs2[0] and Univs2[1]', id(Univs2[0]), id(Univs2[1]))
# Techs.append('RPI')
# print('Univs1 =', Univs1)
# print('Univs2 =', Univs2)
# print(Univs1 == Univs2)          # test value equality
# for e in Univs1:
#     print('Univs contains', e)
#     print(' which contains')
#     for u in e:
#         print('    ', u)

# # Page 81
# L1 = [1, 2, 3]
# L2 = [4, 5, 6]
# L3 = L1 + L2
# print('L3 =', L3)
# L1.extend(L2)
# print('extended L1 =', L1)

# # # Page 82 ~ 83
# def removeDups1(L1, L2):
#     """ Assumes that L1 and L2 are lists
#         Remove any element from L1 that also occurs in L2 """
#     for e1 in L1:
#         if e1 in L2:
#             L1.remove(e1)
# L1 = [1, 2, 3, 4]
# L2 = [1, 2, 5, 6]
# removeDups1(L1, L2)
# print('L1 =', L1)
# def removeDups2(L1, L2):
#     for e1 in L1[:]:
#         if e1 in L2:
#             L1.remove(e1)
# L1 = [1, 2, 3, 4]
# L2 = [1, 2, 5, 6]
# removeDups2(L1, L2)
# print('L1 =', L1)
# def removeDups3(L1, L2):
#     for e1 in list(L1):
#         if e1 in L2:
#             L1.remove(e1)
# L1 = [1, 2, 3, 4]
# L2 = [1, 2, 5, 6]
# removeDups3(L1, L2)
# print('L1 =', L1)

# # Page 84
# print([x**2 for x in range(1,7)])
# mixed = [1, 2, 'a', 3, 4.0]
# print([x**2 for x in mixed if type(x) == int])
# print([x**2 for x in mixed if type(x) == float])

# # Page 85
# def applyToEach(L, f):
#     """ Assumes L is a list, f a function
#         Mutates L by replacing each element, e, of L by f(e) """
#     for i in range(len(L)):
#         L[i] = f(L[i])
# L = [1, -2, 3.33]
# print('L =', L)
# print('Apply abs to each element of L.')
# applyToEach(L, abs)
# print('L =', L)
# print('Apply int to each element of L.')
# applyToEach(L, int)
# print('L =', L)

# # Page 86 ~ 87
# for i in map(abs, [1, -2, 3.33]):
#     print(i)
# L1 = [1, 28, 36]
# L2 = [2, 57, 9]
# for i in map(min, L1, L2):
#     print(i)
# L = []
# for i in map(lambda x, y: x**y, [1, 2, 4, 5], [3, 2, 1, 0]):
#     L.append(i)
# print(L)

# # Page 88
# def splitTest(S, C):
#     """ Assumes S is string, C is list of character
#         return R is S split by c """
#     for c in C:
#         R = S.split(c)
#         print(R)
# splitTest("My favorite professor--John G.--rocks", [' ', '-', '--'])

# # Page 91
EtoF = {'bread':'pain', 'wine':'vin', 'with':'avec', 'I':'Je',
        'eat':'mange', 'drink':'bois', 'John':'Jean',
        'friends':'amis', 'and': 'et', 'of':'du','red':'rouge'}
FtoE = {'pain':'bread', 'vin':'wine', 'avec':'with', 'Je':'I',
        'mange':'eat', 'bois':'drink', 'Jean':'John',
        'amis':'friends', 'et':'and', 'du':'of', 'rouge':'red'}
dicts = {'English to French':EtoF, 'French to English':FtoE}
def translate_word(word, dictionary):
    if word in dictionary.keys():
        return dictionary[word]
    elif word != '':
        return '"' + word + '"'
    return word
def translate(phrase, dicts, direction):
    UC_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LC_letters = 'abcdefghijklmnopqrstuvwxyz'
    letters = UC_letters + LC_letters
    dictionary = dicts[direction]
    translation = ''
    word = ''
    for c in phrase:
        if c in letters:
            word = word + c
        else:
            translation = translation + translate_word(word, dictionary) + c
            word = ''
    return translation + ' ' + translate_word(word, dictionary)
# def translate(phrase, dicts, direction):
#     UC_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     LC_letters = 'abcdefghijklmnopqrstuvwxyz'
#     punctuation = '.,;:?'
#     letters = UC_letters + LC_letters
#     dictionary = dicts[direction]
#     translation = ''
#     word = ''
#     for c in phrase:
#         if c in letters:
#             word = word + c
#         elif word != '':
#             if c in punctuation:
#                 c = c + ' '
#             translation = translation + translate_word(word, dictionary) + c
#             word = ''
#     return translation + ' ' + translate_word(word, dictionary)
print(translate('I drink good red wine, and eat bread. !@#$',
                dicts,'English to French'))
print(translate('Je bois du vin rouge. !@#$',
                dicts, 'French to English'))

# # page 92 ~ 93
# monthNumbers = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5,
#                 1:'I', 2:'II', 3:'III', 4:'IV', 5:'V'}
# keys = []
# for e in monthNumbers:
#     keys.append(str(e))
# print(keys)
# print(monthNumbers)
# months = monthNumbers.keys()
# print(months)
# m = list(months)
# print(m)