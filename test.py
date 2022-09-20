import pylab

def findPayment(loan, r, m):
    return loan * ((r*(1+r)**m) / ((1+r)**m - 1))

class Mortgage(object):
    """ Abstract class for building different kinds of mortgages """
    def __init__(self, loan, annRate, months):
        self.loan = loan
        self.rate = annRate / 12.0
        self.months = months
        self.paid = [0.0]
        self.outstanding = [loan]
        self.payment = findPayment(loan, self.rate, months)
        self.legend = None
    def makePayment(self):
        self.paid.append(self.payment)
        reduction = self.payment - self.outstanding[-1]*self.rate
        self.outstanding.append(self.outstanding[-1] - reduction)
    def getTotalPaid(self):
        return sum(self.paid)
    def __str(self):
        return self.legend
    
    def plotPayments(self, style):
        pylab.plot(self.paid[1:], style, label = self.legend)
    def plotBalance(self, style):
        pylab.plot(self.outstanding, style, label = self.legend)
    def plotTotPd(self, style):
        totPd = [self.paid[0]]
        for i in range(1, len(self.paid)):
            totPd.append(totPd[-1] + self.paid[i])
        pylab.plot(totPd, style, label = self.legend)
    def plotNet(self, style):
        totPd = [self.paid[0]]
        for i in range(1, len(self.paid)):
            totPd.append(totPd[-1] + self.paid[i])
        equityAcquired = pylab.array([self.loan] * len(self.outstanding))
        equityAcquired = equityAcquired - pylab.array(self.outstanding)
        net = pylab.array(totPd) - equityAcquired
        pylab.plot(net, style, label = self.legend)


class Fixed(Mortgage):
    def __init__(self, loan, r, months):
        Mortgage.__init__(self, loan, r, months)
        self.legend = 'Fixed, ' + str(round(r*100, 2)) + '%'

class TwoRate(Mortgage):
    def __init__(self, loan, r, months, teaserRate, teaserMonths):
        Mortgage.__init__(self, loan, teaserRate, months)
        self.teaserMonths = teaserMonths
        self.teaserRate = teaserRate
        self.nextRate = r / 12
        self.legend = str(teaserRate*100) + '% for ' + str(self.teaserMonths) + ' months, then ' + str(round(r*100, 2)) + '%'
    def makePayment(self):
        if len(self.paid) == self.teaserMonths + 1:
            self.rate = self.nextRate
            self.payment = findPayment(self.outstanding[-1], self.rate, self.months - self.teaserMonths)
        Mortgage.makePayment(self)

def plotMortgages(morts, amt):
    def labelPlot(figure, title, xLabel, yLabel):
        pylab.figure(figure)
        pylab.title(title)
        pylab.xlabel(xLabel)
        pylab.ylabel(yLabel)
        pylab.legend(loc = 'best')
    styles = ['k-', 'k:']
    #Give names to figure numbers
    payments, cost, balance, net_cost = 0, 1, 2, 3
    for i in range(len(morts)):
        pylab.figure(payments)
        morts[i].plotPayments(styles[i])
        pylab.figure(cost)
        morts[i].plotTotPd(styles[i])
        pylab.figure(balance)
        morts[i].plotBalance(styles[i])
        pylab.figure(net_cost)
        morts[i].plotNet(styles[i])
    labelPlot(payments, f'Monthly Payments of ${amt:,} Mortages',
               'Months', 'Monthly Payments')
    labelPlot(cost, f'Cash Outlay of ${amt:,} Mortgages',
               'Months', 'Total Payments')
    labelPlot(balance, f'Balance Remaining of ${amt:,} Mortages',
               'Months', 'Remaining Loan Balance of $')
    labelPlot(net_cost, f'Net Cost of ${amt:,} Mortgages',
              'Months', 'Payments - Equity $')

def compareMortgages(amt, years, fixedRate, varRate1, varRate2, varMonths):
    totMonts = years * 12
    fixed1 = Fixed(amt, fixedRate, totMonts)
    twoRate = TwoRate(amt, varRate2, totMonts, varRate1, varMonths)
    morts = [fixed1, twoRate]
    for m in range(totMonts):
        for mort in morts:
            mort.makePayment()
    plotMortgages(morts, amt)
    pylab.show()

compareMortgages(amt=200000, years=30, fixedRate=0.07, \
                  varRate1=0.045, \
                  varRate2=0.095, varMonths=48)
