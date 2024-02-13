from django.urls import path
from administration import views

urlpatterns = [

    # Users
    path('users/', views.AdminUserList.as_view(), name='admin-users'),
    path('users/<int:id>/', views.AdminUserDetail.as_view(), name='admin-user-detail'),

    # Products
    path('products/', views.AdminProductList.as_view(), name='admin-products'),
    path('products/<int:id>/', views.AdminProductDetail.as_view(), name='admin-product-detail'),

    # Reviews
    path('reviews/', views.AdminReviewList.as_view(), name='admin-reviews'),
    path('reviews/<int:id>/', views.AdminReviewDetail.as_view(), name='admin-review-detail'),

    # Orders
    path('orders/', views.AdminOrderList.as_view(), name='admin-orders'),
    path('orders/<int:id>/', views.AdminOrderDetail.as_view(), name='admin-order-detail'),

]