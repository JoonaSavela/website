from django import forms

class InvestingForm(forms.Form):
    initialAmount = forms.IntegerField(required=True, min_value=0, label='Initial Amount')
    years = forms.IntegerField(required=True, min_value=0, label='Years')
