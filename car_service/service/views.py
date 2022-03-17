from datetime import date, timedelta
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator
from django.conf import settings
from django.db.models import Q
from django.views import generic
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect, render, get_object_or_404
from django.utils.translation import gettext_lazy as _
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
        'num_models': num_models,
        'num_car_instances': num_car_instances,
        'num_services': num_services,
        'num_orders_completed': num_orders_completed,
        'num_visits': num_visits,
    }
    return render(request, 'service/index.html', context=context)


class CarInstanceListView(LoginRequiredMixin, generic.ListView):
    model = CarInstance
    template_name = 'service/car_instance_list.html'
    context_object_name = 'car_instances'
    queryset = CarInstance.objects.all()
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_superuser and not self.request.user.is_staff:
            queryset = queryset.filter(owner=self.request.user)
        return queryset

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context


class CarInstanceDetailView(generic.DetailView):
    model = CarInstance
    context_object_name = 'car_instance_detail'
    template_name = 'service/car_instance_detail.html'

    def get_success_url(self):
        return reverse_lazy('service:car-instance-detail', kwargs={'pk': self.object.id})


class OrderListView(LoginRequiredMixin, generic.ListView):
    model = Order
    template_name = 'service/order_list.html'
    context_object_name = 'orders'
    queryset = Order.objects.all()
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_superuser and not self.request.user.is_staff:
            queryset = queryset.filter(car_instance__owner=self.request.user)
        return queryset


class OrderDetailView(generic.DetailView):
    model = Order
    context_object_name = 'order'
    template_name = 'service/order_detail.html'


def search_cars(request):
    query = request.GET.get('query')
    search_results = CarInstance.objects.filter(
        Q(model__model__icontains=query) |
        Q(owner__first_name__icontains=query) |
        Q(registration__icontains=query) |
        Q(vin__icontains=query)
    )
    context = {
        'cars': search_results,
        'query': query
    }
    return render(request, 'service/search_cars.html', context=context)
