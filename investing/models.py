from django.db import models

class InvestmentModel(models.Model):
    years = models.IntegerField(default=10)
    annualInterestRate = models.FloatField(default=1.07)
    monthlyAmount = models.FloatField(default=1500)
    initialCapital = models.FloatField(default=10_000)

    carPrice = models.FloatField(default=71_228)
    carLoanAnnualInterestRate = models.FloatField(default=1.019)
    monthlyCarLoanPayment = models.FloatField(default=614)
    payWithInitialCapital = models.BooleanField(default=False)

    def geomSum(self, a, q, k):
        if q == 1:
            return a * k
        return a * (1 - q ** k) / (1 - q)

    def capitalGain(self, c, q, k):
        return c * q ** k

    def getTime(self):
        base = self.carLoanAnnualInterestRate ** (1 / 12)
        frac = self.monthlyCarLoanPayment / (self.carPrice * (1 - base) + self.monthlyCarLoanPayment)
        return log(frac, base)

    def getTimeSeries(self):
        yearVector = list(range(self.years + 1))
        carLoanVector = []
        capitalVector = []

        capital = self.initialCapital
        carLoan = self.carPrice

        if self.payWithInitialCapital:
            newCarLoan = max(carLoan - capital, 0)
            capital -= carLoan - newCarLoan
            carLoan = newCarLoan

        for year in yearVector:
            carLoanVector.append(carLoan)
            capitalVector.append(capital)

            yearlyCarLoanPayment = min(self.monthlyCarLoanPayment * 12, carLoan)
            carLoan -= yearlyCarLoanPayment
            carLoan *= self.carLoanAnnualInterestRate

            yearlyAmount = self.monthlyAmount * 12 - yearlyCarLoanPayment
            capital += yearlyAmount
            capital *= self.annualInterestRate

        res = {
            'years': yearVector,
            'carLoans': carLoanVector,
            'capitals': capitalVector,
        }

        return res
