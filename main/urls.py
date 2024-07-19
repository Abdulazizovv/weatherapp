from django.urls import path
from . import views

urlpatterns = [
    path('city-suggestions/', views.city_suggestions, name='city_suggestions'),
    path('', views.index, name='index'),
]