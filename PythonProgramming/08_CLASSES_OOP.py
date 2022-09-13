# class IntSet(object):
#     """ An IntSet is a set of integers """
#     # Information about the implementation (not the abstraction)
#     # Value of the set is represented by a list of ints, self.vals.
#     # Each int in the set occurs in self.vals exactly once.
#     def __init__(self):
#         """ Create an empty set of integers """
#         self.vals = []
#     def insert(self, e):
#         """ Assumes e is an integer and insert e into self """
#         if e not in self.vals:
#             self.vals.append(e)
#     def member(self, e):
#         """ Assumes e is an integer
#             Returns True if e is in self, and False otherwise """
#         return e in self.vals
#     def remove(self, e):
#         """ Assume e is an integer and removes e from self
#             Raises ValueError if e is not in self """
#         try:
#             self.vars.remove(e)
#         except:
#             raise ValueError(str(e) + ' not found')
#     def getMembers(self):
#         """ Returns a list containing the elements of self.
#             Nothing can be assumed about the order of the elements """
#         return self.vals[:]
#     def __str__(self):
#         """ Returns a string representation of self """
#         self.vals.sort()
#         result = ''
#         for e in self.vals:
#             result = result + str(e) + ','
#         return '{' + result[:-1] + '}'
# print(type(IntSet), type(IntSet.insert))
# s = IntSet()
# s.insert(3)
# print(s.member(3))
# s.insert(4)
# print(s)
# print(s.__str__())
# print(IntSet.__str__(s))
# print(id(s))

import datetime
class Person(object):
    def __init__(self, name):
        """ Create a person """
        self.name = name
        try:
            lastBlank = name.rindex(' ')
            self.lastName = name[lastBlank+1:]
        except:
            self.lastName = name
        self.birthday = None
    def getName(self):
        """ Return self's full name """
        return self.name
    def getLastName(self):
        """ Return self's last name """
        return self.lastName
    def setBirthday(self, birthdate):
        """ Assumes birthdate is of type datetime.date
            Set self's birthday to birthdate """
        self.birthday = birthdate
    def getAge(self):
        """ Returns self's current age in days """
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days
    def __lt__(self, other):
        """ Returns True if self precedes other in alphabetical order, and False otherwise.
            Comparison is absed on lastnames, but it these are the same full names are compared. """
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
    def __str__(self):
        """ Return self's name """
        return self.name
me = Person("Michael Guttag")
him = Person('Barack Hussein Obama')
her = Person('Madonna')
print(him.getLastName())
him.setBirthday(datetime.date(1961, 8, 4))
her.setBirthday(datetime.date(1958, 8, 16))
print(him.getName(), 'is', him.getAge(), 'days old')
plist = [me, him, her]
for p in plist:
    print(p)
plist.sort()
for p in plist:
    print(p)
    