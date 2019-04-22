from django.shortcuts import render

from .forms import InvestingForm
from .models import InvestmentModel
from .serializers import InvestmentSerializer
from rest_framework import generics
from django.http import Http404
from rest_framework.response import Response

class InvestmentList(generics.ListCreateAPIView):
    queryset = InvestmentModel.objects.all()
    serializer_class = InvestmentSerializer

class InvestmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = InvestmentModel.objects.all()
    serializer_class = InvestmentSerializer

    def get_object(self, pk):
        try:
            return self.queryset.get(pk=pk)
        except InvestmentModel.DoesNotExist:
            raise Http404

    def get(self, request, pk, *args, **kwargs):
        investment = self.get_object(pk)
        serializer = InvestmentSerializer(investment)

        responseDict = investment.getTimeSeries()
        responseDict.update(serializer.data)
        return Response(responseDict)

# Create your views here.
def index(request):
    # show = False
    pk = None
    if request.method == 'POST':
        form = InvestingForm(request.POST)
        if form.is_valid():
            years = form.cleaned_data['years']
            annualInterestRate = form.cleaned_data['annualInterestRate']
            monthlyAmount = form.cleaned_data['monthlyAmount']
            initialCapital = form.cleaned_data['initialCapital']
            carPrice = form.cleaned_data['carPrice']
            carLoanAnnualInterestRate = form.cleaned_data['carLoanAnnualInterestRate']
            monthlyCarLoanPayment = form.cleaned_data['monthlyCarLoanPayment']
            payWithInitialCapital = form.cleaned_data['payWithInitialCapital']
            payCarLoanAfter5Years = form.cleaned_data['payCarLoanAfter5Years']

            obj, created = InvestmentModel.objects.get_or_create(
                years=years,
                annualInterestRate=annualInterestRate,
                monthlyAmount=monthlyAmount,
                initialCapital=initialCapital,
                carPrice=carPrice,
                carLoanAnnualInterestRate=carLoanAnnualInterestRate,
                monthlyCarLoanPayment=monthlyCarLoanPayment,
                payWithInitialCapital=payWithInitialCapital,
                payCarLoanAfter5Years=payCarLoanAfter5Years
            )

            pk = obj.pk

    else:
        form = InvestingForm()

    context = {
        'form': form,
        'pk': pk,
        # 'show': show,
    }
    return render(request, 'investing/index.html', context)
