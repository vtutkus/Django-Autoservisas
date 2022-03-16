from django.contrib import admin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from .models import CarModel, CarInstance, Order, Service, OrderLine


# Register your models here.




admin.site.register(CarModel)
admin.site.register(CarInstance)
admin.site.register(Order)
admin.site.register(Service)
admin.site.register(OrderLine)
admin.site.site_title = _('Car Service Admin')
admin.site.site_header = _('Car Service Administration')
