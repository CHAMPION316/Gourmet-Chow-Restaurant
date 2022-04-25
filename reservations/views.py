from django.shortcuts import render

# Create your views here.


# def view_home(request):
#     """
#     Function enables user to view the home page.
#     """
#     return render(request, 'reservations/index.html')

def view_home(request):
    return render(request, 'index.html')




def add_booking(request):
    return render(request, 'reservations/add_booking.html')



# def main_page(request):
#     return render(request, 'index.html')


# def book_table(request):
#     if request.method=="POST":
#         if request.POST.get('fname') and request.POST.get('lname') and request.POST.get('booking_start'):
#             saveobj=booking()
#             saveobj.fname=request.POST.get('fname')
#             saveobj.lname=request.POST.get('lname')
#             saveobj.booking_start.request.POST.get('booking_start')
#             cursor=connection.cursor("insert into chow316(fname,laname,booking_start) values('"+saveobj.fname+"','"+saveobj.lname+"','"+saveobj.booking_start+"')")
#             messages.success(request,"Your booking "+saveobj.fname+" has been successfully processed.")
#             return render(request, "book.html")
#     else:
#         return render(request, 'book.html')


# def booking_page(request):
#     all_guests = Guest
#     return render(request, 'book.html')
