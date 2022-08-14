from . import views
from django.urls import path

urlpatterns = [
    path('', views.chart, name='helo-world-1'),
]
