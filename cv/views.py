from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'cv/index.html')

def education(request):
    return render(request, 'cv/education.html')
