from django.shortcuts import render
from django.http import HttpResponse
from serpage.models import CustomerData
# Create your views here.

def index(request):
    template_name = 'index.html'
    queryset = CustomerData.objects.all()
    context = {
        "object_List": queryset
    }
    return render(request, template_name, context)
    # resultdisplay=CustomerData.objects.all()



