"""
Url file to allow connection between
different pages in the app.
"""

from django.urls import path
from reservations import views


urlpatterns = [
    path('', views.view_home, name='home'),
    path('add_booking/', views.add_booking, name='add_booking'),
]