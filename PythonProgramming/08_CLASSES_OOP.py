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
from glob import escape
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
# me = Person("Michael Guttag")
# him = Person('Barack Hussein Obama')
# her = Person('Madonna')
# print(him.getLastName())
# him.setBirthday(datetime.date(1961, 8, 4))
# her.setBirthday(datetime.date(1958, 8, 16))
# print(him.getName(), 'is', him.getAge(), 'days old')
# plist = [me, him, her]
# for p in plist:
#     print(p)
# plist.sort()
# for p in plist:
#     print(p)

class MITPerson(Person):
    nextIdNum = 0
    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1
    def getIdNum(self):
        return self.idNum
    def __lt__(self, other):
        return self.idNum < other.idNum
    def isStudent(self):
        return isinstance(self, Student)
# # p1 = MITPerson('Barbara Beaver')
# # print(str(p1) + '\'s id number is ' + str(p1.getIdNum()))
# p1 = MITPerson('Mark Guttag')
# p2 = MITPerson('Billy Bob Beaver')
# p3 = MITPerson('Billy Bob Beaver')
# p4 = Person('Billy Bob Beaver')
# # print(str(p1) + '\'s id number is ' + str(p1.getIdNum()))
# # print('p1 < p2 =', p1 < p2)
# # print('p3 < p2 =', p3 < p2)
# # print('p4 < p1 =', p4 < p1)
# # print('p1 < p4 =', p1 < p4)

class Student(MITPerson):
    pass
class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear
    def getClass(self):
        return self.year
class Grad(Student):
    pass
# p5 = Grad('Buzz Aldrin')
# p6 = UG('Billy Beaver', 1984)
# print(p5, 'is a graduate student is', type(p5) == Grad)
# print(p5, 'is an undergraduate student is', type(p5) == UG)
# print(p5, 'is a student is', p5.isStudent())
# print(p6, 'is a student is', p6.isStudent())
# print(p3, 'is a student is', p3.isStudent())

class Grades(object):
    def __init__(self):
        """ Create empty grade book """
        self.students = []
        self.grades = {}
        self.isSorted = True
    def addStudent(self, student):
        """ Assume: student is of type Student
            Add student to the grade book """
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False
    def addGrade(self, student, grade):
        """ Assumes: grade is a float
            Add grade to the list of grades for student """
        try:
            self.grade[student.getIdNum()].append(grade)
        except:
            raise ValueError('Student not in mapping')
    def getGrades(self, student):
        """ Return a list of grades for student """
        try:
            return self.grades[student.getIdNum()][:]
        except:
            raise ValueError('Student not in mapping')
    def getStudents(self):
        """ Return a sorted list of the students in the grade book """
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        return self.students[:]

def gradeReport(course):
    """ Assumes course is of type Grades """
    report = ''
    for s in course.getStudents():
        tot = 0.0
        numGrades = 0
        for g in course.getGrades(s):
            tot += g
            numGrades += 1
        try:
            average = tot / numGrades
            report = report + '\n' + str(s) + '\'s mean grade is ' + str(average)
        except ZeroDivisionError:
            report = report + '\n' + str(s) + ' has no grades'
    return report

ug1 = UG('Jane Doe', 2014)
ug2 = UG('John Doe', 2015)
ug3 = UG('David Henry', 2003)
g1 = Grad('Billy Buckner')
g2 = Grad('Bucky F. Dent')
print(str(ug1) + '\'s id number is ' + str(ug1.getIdNum()))
print(str(ug2) + '\'s id number is ' + str(ug2.getIdNum()))
print(str(ug3) + '\'s id number is ' + str(ug3.getIdNum()))
print(str(g1) + '\'s id number is ' + str(g1.getIdNum()))
print(str(g2) + '\'s id number is ' + str(g2.getIdNum()))
sixHundred = Grades()
sixHundred.addStudent(ug1)
sixHundred.addStudent(ug2)
sixHundred.addStudent(g1)
sixHundred.addStudent(g2)
print(sixHundred.getStudents()[0].getIdNum())
for s in sixHundred.getStudents():
    sixHundred.addGrade(s, 75)
sixHundred.addGrade(g1, 25)
sixHundred.addGrade(g2, 100)
sixHundred.addStudent(ug3)
print(gradeReport(sixHundred))
