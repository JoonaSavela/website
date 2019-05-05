from django import forms
from django.core.exceptions import ValidationError
# from django.forms.widgets import NumberInput
#
# class RangeInput(NumberInput):
#     input_type = 'range'

class InvestingForm(forms.Form):
    years = forms.IntegerField(min_value=1,
                            label='Years',
                            initial=10,
                            widget=forms.NumberInput(attrs={'class': 'form-control'}))
    annualInterestRate = forms.FloatField(min_value=1.0,
                            label='Annual Interest Rate',
                            initial=1.07,
                            widget=forms.NumberInput(attrs={'class': 'form-control'}))
    monthlyAmount = forms.FloatField(min_value=0,
                            label='Monthly Amount',
                            initial=2000,
                            widget=forms.NumberInput(attrs={'class': 'form-control'}))
    initialCapital = forms.FloatField(min_value=0,
                            label='Initial Capital',
                            initial=10_000,
                            widget=forms.NumberInput(attrs={'class': 'form-control'}))

    carPrice = forms.FloatField(min_value=0,
                            label='Car Price',
                            initial=71_228,
                            widget=forms.NumberInput(attrs={'class': 'form-control'}))
    carLoanAnnualInterestRate = forms.FloatField(min_value=1.0,
                            label='Car Loan Annual Interest Rate',
                            initial=1.019,
                            widget=forms.NumberInput(attrs={'class': 'form-control'}))
    monthlyCarLoanPayment = forms.FloatField(min_value=0,
                            label='Monthly Car Loan Payment',
                            initial=614,
                            widget=forms.NumberInput(attrs={'class': 'form-control'}))
    payWithInitialCapital = forms.BooleanField(label='Pay With Initial Capital',
                            required=False,
                            widget=forms.CheckboxInput(attrs={'class': 'form-control'}))
    payCarLoanAfter5Years = forms.BooleanField(label='Pay Car Loan After 5 Years',
                            required=False,
                            initial=True,
                            widget=forms.CheckboxInput(attrs={'class': 'form-control'}))

    apartmentLoan = forms.FloatField(min_value=0,
                            label='Apartment Loan',
                            initial=100_000,
                            widget=forms.NumberInput(attrs={'class': 'form-control'}))
    apartmentLoanAnnualInterestRate = forms.FloatField(min_value=1.0,
                            label='Apartment Loan Annual Interest Rate',
                            initial=1.0125,
                            widget=forms.NumberInput(attrs={'class': 'form-control'}))
    monthlyApartmentLoanPayment = forms.FloatField(min_value=0,
                            label='Monthly Apartment Loan Payment',
                            initial=500,
                            widget=forms.NumberInput(attrs={'class': 'form-control'}))
    spousePaysEqualAmount = forms.BooleanField(label='Spouse Pays Equal Amount',
                            required=False,
                            widget=forms.CheckboxInput(attrs={'class': 'form-control'}))

    def clean(self):
        cd = self.cleaned_data

        if cd.get('monthlyCarLoanPayment') + cd.get('monthlyApartmentLoanPayment') > cd.get('monthlyAmount'):
            raise ValidationError("Sum of monthly car and apartment loan payments cannot be greater than monthly amount.")

        return cd
