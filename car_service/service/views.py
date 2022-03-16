from django.shortcuts import render
from django.views import generic


# Create your views here.


def index(request):
    return render(request, 'service/index.html')

# class Index(generic.View):
#     template_name = 'service/index.html'
