from django.shortcuts import render

from .forms import InvestingForm

# Create your views here.
def index(request):
    amount = 0
    show = False
    if request.method == 'POST':
        form = InvestingForm(request.POST)
        if form.is_valid():
            initialAmount = form.cleaned_data['initialAmount']
            years = form.cleaned_data['years']
            amount = initialAmount * years * 12
            show = True

    else:
        form = InvestingForm()
    context = {
        'form': form,
        'amount': amount,
        'show': show,
    }
    return render(request, 'investing/index.html', context)
