from django.shortcuts import render
from .models import booking
from django.db import connection
from django.contrib import messages

# Create your views here.


def main_page(request):
    return render(request, 'index.html')


def book_table(request):
    if request.method=="POST":
        if request.POST.get('fname') and request.POST.get('lname') and request.post.get('booking_start'):
            saveobj=booking()
            saveobj.fname=request.POST.get('')
            saveobj.lname=request.POST.get('')
            saveobj.booking_start.request.POST.get('')
            cursor=connection.cursor("insert into chow316(fname,laname,booking_start) values('"+saveobj.fname+"','"+saveobj.lname+"','"+saveobj.booking_start+"')")
            messages.success(request,"Your booking "+saveobj.fname+" has been successfully processed.")
            return render(request, "book.html")
    else:
        return render(request, 'book.html')


# def booking_page(request):
#     all_guests = Guest
#     return render(request, 'book.html')
