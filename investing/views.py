from django.shortcuts import render
from math import log

from .forms import InvestingForm

def geomSum(a, q, k):
    if q == 1:
        return a * k
    return a * (1 - q ** k) / (1 - q)

def capitalGain(c, q, k):
    return c * q ** k

def getTime(monthlyCarLoanPayment, carPrice, carLoanAnnualInterestRate):
    base = carLoanAnnualInterestRate ** (1 / 12)
    frac = monthlyCarLoanPayment / (carPrice * (1 - base) + monthlyCarLoanPayment)
    return log(frac, base)

# Create your views here.
def index(request):
    amount = 0
    show = False
    years = 0
    months = 0
    carLoanInterestPaid = 0
    if request.method == 'POST':
        form = InvestingForm(request.POST)
        if form.is_valid():
            annualInterestRate = form.cleaned_data['annualInterestRate']
            monthlyAmount = form.cleaned_data['monthlyAmount']
            capital = form.cleaned_data['initialCapital']
            carPrice = form.cleaned_data['carPrice']
            carLoanAnnualInterestRate = form.cleaned_data['carLoanAnnualInterestRate']
            monthlyCarLoanPayment = form.cleaned_data['monthlyCarLoanPayment']
            payWithInitialCapital = form.cleaned_data['payWithInitialCapital']

            if payWithInitialCapital:
                newCarPrice = max(carPrice - capital, 0)
                capital -= carPrice - newCarPrice
                carPrice = newCarPrice

            months = getTime(monthlyCarLoanPayment, carPrice, carLoanAnnualInterestRate)

            carLoanInterestPaid = round(months * monthlyCarLoanPayment - carPrice, 2)

            years = round(months // 12)
            months = round(months - years * 12)

            amount = geomSum(monthlyAmount - monthlyCarLoanPayment, annualInterestRate ** (1 / 12), years * 12 + months)
            amount += capitalGain(capital, annualInterestRate ** (1 / 12), years * 12 + months)

            show = True
    else:
        form = InvestingForm()

    context = {
        'form': form,
        'years': years,
        'months': months,
        'amount': round(amount, 2),
        'carLoanInterestPaid': carLoanInterestPaid,
        'show': show,
    }
    return render(request, 'investing/index.html', context)
