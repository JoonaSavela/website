from django import forms
from django.core.exceptions import ValidationError

class InvestingForm(forms.Form):
    years = forms.IntegerField(required=True,
                            min_value=1,
                            label='Years',
                            initial=10,
                            widget=forms.NumberInput(attrs={'class': 'form-control'}))
    annualInterestRate = forms.FloatField(required=True,
                            min_value=1.0,
                            label='Annual Interest Rate',
                            initial=1.07,
                            widget=forms.NumberInput(attrs={'class': 'form-control'}))
    monthlyAmount = forms.FloatField(required=True,
                            min_value=0,
                            label='Monthly Amount',
                            initial=1500,
                            widget=forms.NumberInput(attrs={'class': 'form-control'}))
    initialCapital = forms.FloatField(required=True,
                            min_value=0,
                            label='Initial Capital',
                            initial=10_000,
                            widget=forms.NumberInput(attrs={'class': 'form-control'}))

    carPrice = forms.FloatField(required=True,
                            min_value=0,
                            label='Car Price',
                            initial=71_228,
                            widget=forms.NumberInput(attrs={'class': 'form-control'}))
    carLoanAnnualInterestRate = forms.FloatField(required=True,
                            min_value=1.0,
                            label='Car Loan Annual Interest Rate',
                            initial=1.019,
                            widget=forms.NumberInput(attrs={'class': 'form-control'}))
    monthlyCarLoanPayment = forms.FloatField(required=True,
                            min_value=0,
                            label='Monthly Car Loan Payment',
                            initial=614,
                            widget=forms.NumberInput(attrs={'class': 'form-control'}))
    payWithInitialCapital = forms.BooleanField(label='Pay With Initial Capital',
                            required=False,
                            widget=forms.CheckboxInput(attrs={'class': 'form-control'}))

    def clean(self):
        cd = self.cleaned_data

        if cd.get('monthlyCarLoanPayment') > cd.get('monthlyAmount'):
            raise ValidationError("Monthly car loan payment cannot be grater than monthly amount.")

        return cd
