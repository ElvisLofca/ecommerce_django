from django.urls import path
from reviews import views

urlpatterns = [
    path('', views.ReviewList.as_view(), name='reviews'),
    path('<int:id>/', views.ReviewDetail.as_view(), name='review-detail'),
]