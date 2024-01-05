from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.UserView.as_view()),
    path('register/', views.RegisterView.as_view()),
    path('sendemail/', views.EmailAPIView.as_view()),
]
