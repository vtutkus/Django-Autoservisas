from django.urls import path
from . import views

app_name = 'service'
urlpatterns = [
    path('', views.index, name='index'),
    # path('authors/', views.authors, name='authors'),
    # path('author/<int:author_id>', views.author, name='author'),  
    path('orders/', views.OrderListView.as_view(), name='orders'),
    path('orders/<int:pk>', views.OrderDetailView.as_view(), name='order-detail'),

    path('car_instances/', views.CarInstanceListView.as_view(), name='car-instances'),
    path('car_instances/<int:pk>', views.CarInstanceDetailView.as_view(), name='car-instance-detail'),
    path('car_instances/search/', views.search_cars, name='car-instance-search'),
    # path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-books'),
    # path('mybooks/new/', views.BookByUserCreateView.as_view(), name='my-new-book-instance'),
    # path('mybooks/<uuid:pk>/update/', views.BookByUserUpdateView.as_view(), name='update-my-book-instance'),
    # path('mybooks/<uuid:pk>/delete/', views.BookByUserDeleteView.as_view(), name='delete-my-book-instance'),

]
