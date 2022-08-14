from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def chart(request):
    return render(request, 'chart.html')
