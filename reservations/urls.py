"""
Url file to allow connection between
different pages in the app.
"""

from django.urls import path
from restaurant import views


urlpatterns = [
    path('', views.view_home, name='home'),
    path('menu/', views.view_menu, name='menu'),
    path('add_booking/', views.add_booking, name='add_booking'),
    path('contact', views.contact, name='contact'),
]