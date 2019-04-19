from rest_framework import serializers
from .models import InvestmentModel

class InvestmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestmentModel
        fields = ('id',
                  'annualInterestRate',
                  'monthlyAmount',
                  'initialCapital',
                  'carPrice',
                  'carLoanAnnualInterestRate',
                  'monthlyCarLoanPayment',
                  'payWithInitialCapital',)
