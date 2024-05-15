from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_dashboard, name='my-dashboard')
]