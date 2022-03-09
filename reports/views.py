from multiprocessing import context
from re import template
from django.shortcuts import render

# Create your views here.


def homeView(request):
    template_name = 'reports/home.html'
    context = {
        'name': "Reports!"
    }
    return render(request, template_name, context)
