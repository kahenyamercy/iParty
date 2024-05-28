from django.urls import path
from . import views

app_name = 'bookings'

urlpatterns = [
    path('my-bookings/', views.booking_list, name='user_bookings'),
    path('event/<int:pk>/', views.event_bookings, name='event_bookings'),
    path('book/<int:pk>/', views.book_event, name='book_event'),
    path('detail/<int:pk>/', views.booking_detail, name='booking_detail'),
    path('cancel/<int:pk>/', views.cancel_booking, name='cancel_booking'),
]
