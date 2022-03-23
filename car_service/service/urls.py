from django.urls import path
from . import views

app_name = 'service'
urlpatterns = [
    path('', views.index, name='index'),

    path('orders/', views.OrderListView.as_view(), name='orders'),
    path('orders/<int:pk>', views.OrderDetailView.as_view(), name='order-detail'),

    path('car_instances/', views.CarInstanceListView.as_view(), name='car-instances'),
    path('car_instances/<int:pk>', views.CarInstanceDetailView.as_view(),
         name='car-instance-detail'),
    path('car_instances/search/', views.search_cars, name='car-instance-search'),
    path('orders/new/', views.CreateOrderView.as_view(), name='create-order'),
    path('orders/<int:pk>/update/',
         views.UpdateOrderView.as_view(), name='update-order'),
    path('orders/<int:pk>/delete/',
         views.DeleteOrderView.as_view(), name='delete-order'),

]
