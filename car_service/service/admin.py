from django.contrib import admin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from .models import CarModel, CarInstance, Order, Service, OrderLine


# Register your models here.

class OrderLineInline(admin.TabularInline):
    model = OrderLine
    fields = ('order', 'service', 'quantity', 'price')
    readonly_fields = ('id',)
    can_delete = True
    extra = 0

class CarModelAdmin(admin.ModelAdmin):
    list_display = ('make', 'model')
    list_display_links = ('model',)
    list_filter = ('make',)
    search_fields = ('make', 'model')


class CarInstanceAdmin(admin.ModelAdmin):
    list_display = ('registration', 'model', 'owner', 'vin')
    list_display_links = ('registration',)
    list_filter = ('owner','model',)
    search_fields = ('registration', 'vin')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'status', 'car_instance', 'sum')
    list_display_links = ('created_at',)
    list_filter = ('car_instance',)
    search_fields = ('car_instance',)
    inlines = (OrderLineInline, )



class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',)
    list_display_links = ('name',)
    # list_filter = ('car_instance',)
    search_fields = ('name',)

class OrderLineAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'service', 'quantity', 'price')
    list_display_links = ('id',)
    list_filter = ('order', 'service',)
    search_fields = ('order', 'service',)



admin.site.register(CarModel, CarModelAdmin)
admin.site.register(CarInstance, CarInstanceAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(OrderLine, OrderLineAdmin)
admin.site.site_title = _('Car Service Admin')
admin.site.site_header = _('Car Service Administration')
