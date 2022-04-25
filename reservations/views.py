from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking

def handler404(request, *args, **argv):
    """
    A Function to trigger a 404 error
    page in production environment if booking is not found.
    """
    form = BookingForm()
    context = {
        'form': form
        }
    response = render(request, 'restaurant/not_found.html', context)
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    """
    Function to enable customizing 404 error page
    in production environment if booking is duplicate.
    """
    bookings = Booking.objects.all()
    context = {
        'bookings': bookings
    }
    response = render(request, 'restaurant/duplicate_booking.html', context)
    response.status_code = 500
    return response


def view_home(request):
    """
    Function enables user to view the home page.
    """
    return render(request, 'restaurant/index.html')


def view_menu(request):
    """
    Function enables user to view the menu page.
    """
    return render(request, 'restaurant/menu.html')


def contact(request):
    """
    Function enables user to view the menu page.
    """
    return render(request, 'restaurant/contact.html')


@login_required
def add_booking(request):
    """
    Function that allows the user to
    create a booking and add it 
    to the database.
    """
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            booking.user = request.user
            booking.save()
            messages.success(request, 'Booking completed.')
            return redirect('view_booking')
        else:
            messages.error(request, 'Please book with a future date.')
    form = BookingForm()
    context = {
        'form': form
        }
    return render(request, 'restaurant/add_booking.html', context)