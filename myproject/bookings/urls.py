from django.urls import path
from . import views

app_name = 'bookings'

urlpatterns = [
    path('', views.booking_list, name='booking_list'),
    path('event/<int:pk>/bookings/', views.event_bookings, name='event_bookings'),  # Bookings for a specific event
    path('event/<int:pk>/book/', views.book_event, name='book_event'),  # Book an event
    path('<int:pk>/', views.booking_detail, name='booking_detail'),  # Booking detail
    path('<int:pk>/cancel/', views.cancel_booking, name='cancel_booking'),  # Cancel booking
]
