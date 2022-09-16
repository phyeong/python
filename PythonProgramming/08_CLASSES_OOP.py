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

# import datetime
# class Person(object):
#     def __init__(self, name):
#         """ Create a person """
#         self.name = name
#         try:
#             lastBlank = name.rindex(' ')
#             self.lastName = name[lastBlank+1:]
#         except:
#             self.lastName = name
#         self.birthday = None
#     def getName(self):
#         """ Return self's full name """
#         return self.name
#     def getLastName(self):
#         """ Return self's last name """
#         return self.lastName
#     def setBirthday(self, birthdate):
#         """ Assumes birthdate is of type datetime.date
#             Set self's birthday to birthdate """
#         self.birthday = birthdate
#     def getAge(self):
#         """ Returns self's current age in days """
#         if self.birthday == None:
#             raise ValueError
#         return (datetime.date.today() - self.birthday).days
#     def __lt__(self, other):
#         """ Returns True if self precedes other in alphabetical order, and False otherwise.
#             Comparison is absed on lastnames, but it these are the same full names are compared. """
#         if self.lastName == other.lastName:
#             return self.name < other.name
#         return self.lastName < other.lastName
#     def __str__(self):
#         """ Return self's name """
#         return self.name
# # me = Person("Michael Guttag")
# # him = Person('Barack Hussein Obama')
# # her = Person('Madonna')
# # print(him.getLastName())
# # him.setBirthday(datetime.date(1961, 8, 4))
# # her.setBirthday(datetime.date(1958, 8, 16))
# # print(him.getName(), 'is', him.getAge(), 'days old')
# # plist = [me, him, her]
# # for p in plist:
# #     print(p)
# # plist.sort()
# # for p in plist:
# #     print(p)

# class MITPerson(Person):
#     nextIdNum = 0
#     def __init__(self, name):
#         Person.__init__(self, name)
#         self.idNum = MITPerson.nextIdNum
#         MITPerson.nextIdNum += 1
#     def getIdNum(self):
#         return self.idNum
#     def __lt__(self, other):
#         return self.idNum < other.idNum
#     # def isStudent(self):
#     #     return isinstance(self, Student)
# # # p1 = MITPerson('Barbara Beaver')
# # # print(str(p1) + '\'s id number is ' + str(p1.getIdNum()))
# # p1 = MITPerson('Mark Guttag')
# # p2 = MITPerson('Billy Bob Beaver')
# # p3 = MITPerson('Billy Bob Beaver')
# # p4 = Person('Billy Bob Beaver')
# # # print(str(p1) + '\'s id number is ' + str(p1.getIdNum()))
# # # print('p1 < p2 =', p1 < p2)
# # # print('p3 < p2 =', p3 < p2)
# # # print('p4 < p1 =', p4 < p1)
# # # print('p1 < p4 =', p1 < p4)

# class Student(MITPerson):
#     pass
# class UG(Student):
#     def __init__(self, name, classYear):
#         MITPerson.__init__(self, name)
#         self.year = classYear
#     def getClass(self):
#         return self.year
# class Grad(Student):
#     pass
# # p5 = Grad('Buzz Aldrin')
# # p6 = UG('Billy Beaver', 1984)
# # print(p5, 'is a graduate student is', type(p5) == Grad)
# # print(p5, 'is an undergraduate student is', type(p5) == UG)
# # print(p5, 'is a student is', p5.isStudent())
# # print(p6, 'is a student is', p6.isStudent())
# # print(p3, 'is a student is', p3.isStudent())

# class Grades(object):
#     def __init__(self):
#         """ Create empty grade book """
#         self.students = []
#         self.grades = {}
#         self.isSorted = True
#     def addStudent(self, student):
#         """ Assume: student is of type Student
#             Add student to the grade book """
#         if student in self.students:
#             raise ValueError('Duplicate student')
#         self.students.append(student)
#         self.grades[student.getIdNum()] = []
#         self.isSorted = False
#     def addGrade(self, student, grade):
#         """ Assumes: grade is a float
#             Add grade to the list of grades for student """
#         try:
#             self.grades[student.getIdNum()].append(grade)
#         except:
#             raise ValueError('Student not in mapping')
#     def getGrades(self, student):
#         """ Return a list of grades for student """
#         try:
# #            print('test getGrades', self.grades[student.getIdNum()][:])
#             return self.grades[student.getIdNum()][:]
#         except:
#             raise ValueError('Student not in mapping')
#     def getStudents(self):
#         """ Return a sorted list of the students in the grade book """
#         if not self.isSorted:
#             self.students.sort()
#             self.isSorted = True
#         return self.students[:]
#     # def getStudents(self):
#     #     """ Return the students in the grade book one at a time in alphabetical order """
#     #     if not self.isSorted:
#     #         self.students.sort()
#     #         self.isSorted = True
#     #     for s in self.students:
#     #         yield s
        
# def gradeReport(course):
#     """ Assumes course is of type Grades """
#     report = ''
#     for s in course.getStudents():
#         tot = 0.0
#         numGrades = 0
#         for g in course.getGrades(s):
# #            print("test gradeReport g", g)
#             tot += g
#             numGrades += 1
#         try:
#             average = tot / numGrades
#             report = report + '\n' + str(s) + '\'s mean grade is ' + str(average)
#         except ZeroDivisionError:
#             report = report + '\n' + str(s) + ' has no grades'
#     return report

# ug1 = UG('Jane Doe', 2014)
# ug2 = UG('John Doe', 2015)
# ug3 = UG('David Henry', 2003)
# g1 = Grad('Billy Buckner')
# g2 = Grad('Bucky F. Dent')
# sixHundred = Grades()
# sixHundred.addStudent(ug1)
# sixHundred.addStudent(ug2)
# sixHundred.addStudent(g1)
# sixHundred.addStudent(g2)
# for s in sixHundred.getStudents():
#     sixHundred.addGrade(s, 75)
# sixHundred.addGrade(g1, 25)
# sixHundred.addGrade(g2, 100)
# sixHundred.addStudent(ug3)
# print(gradeReport(sixHundred))

# class infoHiding(object):
#     def __init__(self):
#         self.visible = 'Look at me'
#         self.__alsoVisible__ = 'Look at me too'
#         self.__invisible = 'Don\'t look at me directly'
#     def printVisible(self):
#         print(self.visible)
#     def printInvisible(self):
#         print(self.__invisible)
#     def __printInvisible(self):
#         print(self.__invisible)
#     def __printInvisible__(self):
#         print(self.__invisible)
# test = infoHiding()
# # # print(test.visible)
# # # print(test.__alsoVisible__)
# # # print(test.__invisible)
# # test.printInvisible()
# # test.printInvisible()
# # test.__printInvisible__()
# # test.__printInvisible()

# class subClass(infoHiding):
#     def __init__(self):
#         print('from subclass', self.__invisible)
# testSub = subClass()

# def findPayment(loan, r, m):
#     """ Assumes : loan and r are floats, m an int 
#         Returns the monthly payment for a mortgage of size loan
#         at a monthly rate of r for m months """
#     return loan * ((r * (1+r)**m) / ((1+r)**m -1))
# # payment = findPayment(1000000, 0.01, 12)
# # print('monthly payment :', round(payment), 'total paymentt :', round(payment*12))

# class Mortgage(object):
#     """ Abstract class for building different kinds of mortgage """
#     def __init__(self, loan, annRate, months):
#         """ Assumes: lona and annRate are floats, months an int 
#             Creates a new mortgage of size loan, duration months, and annual rate annRate """
#         self.loan = loan
#         self.rate = annRate / 12
#         self.months = months
#         self.paid = [0.0]
#         self.outstanding = [loan]
#         self.payment = findPayment(loan, self.rate, months)
#         self.legend = None
#     def makePayment(self):
#         """ Make a payment """
#         self.paid.append(self.payment)
#         reduction = self.payment - self.outstanding[-1] * self.rate
#         self.outstanding.append(self.outstanding[-1] - reduction)
#     def getTotalPaid(self):
#         """ Return the total amount paid so far """
#         return sum(self.paid)
#     def __str__(self):
#         return self.legend
# # t = Mortgage(1000000, 0.12, 12)
# # for i in range(12):
# #     t.makePayment()
# # tp = t.getTotalPaid()
# # print(tp)

# class Fixed(Mortgage):
#     def __init__(self, loan, r, months):
#         Mortgage.__init__(self, loan, r, months)
#         # super().__init__(loan, r, months)
#         self.legend = 'Fixed, ' + str(round(r*100, 2)) + '%'
# t = Fixed(1000000, 0.12, 12)
# for i in range(12):
#     t.makePayment()
# tp = t.getTotalPaid()
# print(tp)

# class FixedWithPts(Mortgage):
#     def __init__(self, loan, r, months, pts):
#         Mortgage.__init__(self, loan, r, months)
#         self.pts = pts
#         self.paid = [loan * (pts / 100)]
#         self.legend = 'Fixed, ' + str(round(r*100, 2)) + '%, ' + str(pts) + ' points'
# # t = FixedWithPts(200000, 0.05, 360, 3.25)
# # for i in range(360):
# #     t.makePayment()
# # tp = t.getTotalPaid()
# # print(tp)

# class TwoRate(Mortgage):
#     def __init__(self, loan, r, months, teaserRate, teaserMonths):
#         Mortgage.__init__(self, loan, teaserRate, months)
#         self.teaserMonths = teaserMonths
#         self.teaserRate = teaserRate
#         self.nextRate = r / 12
#         self.legend = str(teaserRate*100) + '% for ' + str(self.teaserMonths) + ' months, then ' + str(round(r*100, 2)) + '%'
#     def makePayment(self):
#         if len(self.paid) == self.teaserMonths + 1:
#             self.rate = self.nextRate
#             self.payment = findPayment(self.outstanding[-1], self.rate, self.months - self.teaserMonths)
#         Mortgage.makePayment(self)

# def compareMortgages(amt, years, fixedRate, pts, ptsRate, varRate1, varRate2, varMonths):
#     totMonts = years * 12
#     fixed1 = Fixed(amt, fixedRate, totMonts)
#     fixed2 = FixedWithPts(amt, ptsRate, totMonts, pts)
#     twoRate = TwoRate(amt, varRate2, totMonts, varRate1, varMonths)
#     morts = [fixed1, fixed2, twoRate]
#     for m in range(totMonts):
#         for mort in morts:
#             mort.makePayment()
#     for m in morts:
#         print(m)
#         print(' Total payments = $' + str(int(m.getTotalPaid())))
# # compareMortgages(amt=200000, years=30, fixedRate=0.07, pts=3.25, ptsRate=0.05, varRate1=0.045, varRate2=0.095, varMonths=48)
# # compareMortgages(amt=100000, years=1, fixedRate=0.05, pts=0.0, ptsRate=0.05, varRate1=0.05, varRate2=0.05, varMonths=6)
# # compareMortgages(amt=100000, years=1, fixedRate=0.05, pts=0.1, ptsRate=0.05, varRate1=0.05, varRate2=0.05, varMonths=6)
