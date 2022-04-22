from django.shortcuts import render
from .models import Guest

# Create your views here.


def main_page(request):
    return render(request, 'index.html')


def booking_page(request):
    all_guests = Guest
    return render(request, 'book.html')