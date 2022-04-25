from django.shortcuts import render, redirect, get_object_or_404


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