from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking
from events.models import Event
from django.contrib import messages  # Import messages

def booking_list(request):
    bookings = Booking.objects.all().order_by('-created_at')  # Order by recent first
    context = {'bookings': bookings}
    return render(request, 'booking_list.html', context)

def event_bookings(request, pk):
    event = get_object_or_404(Event, pk=pk)
    bookings = Booking.objects.filter(event=event)  # Filter bookings for this event
    context = {'event': event, 'bookings': bookings}
    return render(request, 'event_bookings.html', context)

def book_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        # Handle booking form submission (implement form validation)
        if event.has_available_seats():  # Check for available seats before booking
            booking = Booking.objects.create(event=event, user=request.user)  # Create booking
            # Handle transaction creation if applicable (integrate with transactions app)
            messages.success(request, 'You have successfully booked the event!')
            return redirect('event_detail', pk=pk)  # Redirect to event detail
        else:
            messages.error(request, 'Event is fully booked. Please try another event.')
    context = {'event': event}
    return render(request, 'book_event.html', context)

def booking_detail(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    context = {'booking': booking}
    return render(request, 'booking_detail.html', context)

def cancel_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        booking.delete()  # Cancel booking and handle transaction if applicable
        messages.success(request, 'Your booking has been canceled successfully!')
        return redirect('booking_list')
    context = {'booking': booking}
    return render(request, 'cancel_booking.html', context)
