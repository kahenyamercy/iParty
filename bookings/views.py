from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Booking
from events.models import Event
from django.contrib import messages
from django.db.models import F
from  .forms import BookingForm

@login_required
def booking_list(request):
    user = request.user
    bookings = Booking.objects.filter(user=user.id).annotate(event_created_at=F('created_at')
    ).order_by('-created_at')
    context = {'bookings': bookings}
    return render(request, 'user_bookings.html', context)

def event_bookings(request, pk):
    event = get_object_or_404(Event, pk=pk)
    bookings = Booking.objects.filter(event=event)  # Filter bookings for this event
    context = {'event': event, 'bookings': bookings}
    return render(request, 'event_bookings.html', context)

@login_required
def book_event(request, pk):
    print(f"Request path: {request.path}")
    event = get_object_or_404(Event, pk=pk)
    user = request.user
    if request.method == 'POST':
        phone = request.POST.get('phone_no')
        print(phone)
        booking_data = {
            "event": event.id,
            "user": user.id
        }
        form = BookingForm(data=booking_data)
        if form.is_valid():
            form.save()
            return redirect('bookings:user_bookings')
    return redirect('app:user_dashboard')

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
