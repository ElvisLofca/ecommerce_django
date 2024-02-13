from django.urls import path
from users import views

urlpatterns = [
    path('<int:id>/', views.UserDetail.as_view(), name='user-detail'),
]