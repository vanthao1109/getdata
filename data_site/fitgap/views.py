from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def fitgap(request):
    return render(request, 'image.html')
