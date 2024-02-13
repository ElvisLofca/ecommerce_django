from django.urls import path
from products import views

urlpatterns = [
    path('', views.ProductList.as_view(), name='products'),
    path('<int:id>/', views.ProductDetail.as_view(), name='product-detail'),
]