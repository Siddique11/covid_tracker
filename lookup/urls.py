from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('countries/', views.countries, name='countries'),
    path('Bangladesh/', views.bd, name='Bangladesh'),
]
