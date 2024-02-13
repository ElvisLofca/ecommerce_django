from django.urls import path
from orders import views

urlpatterns = [
    path('', views.OrderList.as_view(), name='orders'),
    path('<int:id>/', views.OrderDetail.as_view(), name='order-detail'),
]