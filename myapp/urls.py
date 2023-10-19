from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('contact/',views.Contacts,name="contact"),
    path('Booking/',views.Booking,name="booking"),

]
