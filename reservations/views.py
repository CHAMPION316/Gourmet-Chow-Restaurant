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
    response = render(request, 'reservations/not_found.html', context)
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
    response = render(request, 'reservations/duplicate_booking.html', context)
    response.status_code = 500
    return response


def view_home(request):
    """
    Function enables user to view the home page.
    """
    return render(request, 'reservations/index.html')


def view_menu(request):
    """
    Function enables user to view the menu page.
    """
    return render(request, 'reservations/menu.html')


def contact(request):
    """
    Function enables user to view the menu page.
    """
    return render(request, 'reservations/contact.html')


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
    return render(request, 'reservations/add_booking.html', context)


@login_required
def view_booking(request):
    """
    Function that allows the user to view a booking
    after it has been made and added to the database.
    """
    bookings = Booking.objects.filter(user__in=[request.user])
    context = {
        'bookings': bookings
    }
    return render(request, 'reservations/view_booking.html', context)


@login_required
def edit_booking(request, booking_id):
    """
    Function that allows the user to edit a booking
    after it has been made and added to the database.
    """
    book = get_object_or_404(Booking, id=booking_id)
    if request.method == "POST":
        form = BookingForm(request.POST, instance=book)
        if form.is_valid():
            booking = form.save()
            booking.user = request.user
            booking.save()
            messages.success(request, 'Your booking has been updated.')
        return redirect('view_booking')
    form = BookingForm(instance=book)
    context = {
        'form': form
    }
    return render(request, 'reservations/edit_booking.html', context)


@login_required
def delete_booking(request, booking_id):
    """
    Function allows the user to delete a booking
    after it has been made and added to the database.
    """
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)
        if booking.delete():
            messages.success(request, 'Your booking has been deleted.')
            return redirect('view_booking')

    form = BookingForm(instance=booking)
    context = {
        'form': form
    }
    return render(request, 'reservations/delete_booking.html', context)