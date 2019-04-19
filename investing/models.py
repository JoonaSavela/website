from django.db import models

class InvestmentModel(models.Model):
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

    def getTime(self, monthlyCarLoanPayment, carPrice, carLoanAnnualInterestRate):
        base = carLoanAnnualInterestRate ** (1 / 12)
        frac = monthlyCarLoanPayment / (carPrice * (1 - base) + monthlyCarLoanPayment)
        return log(frac, base)

    def getTimeSeries(self):
        return []
