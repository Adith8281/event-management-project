from django.urls import path
from .views import register_view, login_view, logout_view
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/',  views.home, name='home'),
      
]


