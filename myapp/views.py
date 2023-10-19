from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"store/home.html")

def Contacts(request):
    return render(request,"store/contact.html")

def Booking(request):
    return render(request,"store/Bookings.html")