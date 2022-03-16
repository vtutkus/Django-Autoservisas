from django.shortcuts import render
from django.views import generic
from .models import CarModel, CarInstance, Service, Order



# Create your views here.


def index(request):
    num_models = CarModel.objects.count()
    num_car_instances = CarInstance.objects.count()
    num_services = Service.objects.count()
    num_orders_completed = Order.objects.filter(status__exact=30).count()
    num_visits = int(request.session.get('num_visits', 0)) + 1
    request.session['num_visits'] = num_visits
    
    context = {
        'num_models':num_models,
        'num_car_instances':num_car_instances,
        'num_services':num_services,
        'num_orders_completed':num_orders_completed,
        'num_visits':num_visits,
    }
    return render(request, 'service/index.html', context=context)

