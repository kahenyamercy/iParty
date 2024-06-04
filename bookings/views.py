from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import requests
import os
from .models import Booking
from events.models import Event
from django.contrib import messages
from django.db.models import F
from  .forms import BookingForm

API_WAP_BASE_URL = 'https://api.apiwap.com/api/v1'

def send_whatsapp_message(phone_number, message, event_title):
    """
    Send a WhatsApp message using the provided API.

    Parameters:
    api_key (str): The API key for authorization.
    phone_number (str): The recipient's phone number in international format (e.g., +254712345678).
    message (str): The message to send.
    
    Returns:
    dict: The response from the API.
    """
    api_key = os.environ.get('API_WAP_KEY')
    # Define the endpoint URL
    url = f"{API_WAP_BASE_URL}/whatsapp/send-message"

    # Define the headers
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # Define the request payload
    payload = {
        "phoneNumber": phone_number,
        "message": message,
        "type": "media",
        "media_type": "image",
        "fileName": f"{event_title}.jpeg",
        "mediaUrl": "https://thumbs2.imgbox.com/98/22/nqdfXUJi_t.jpeg"
    }

    try:
        # Make the POST request
        response = requests.post(url, headers=headers, json=payload)

        # Check if the request was successful
        response.raise_for_status()

        # Return the JSON response
        return response.json()
    except requests.exceptions.RequestException as e:
        # Print any error that occurs
        print(f"An error occurred: {e}")
        return None

@login_required(login_url='/users/login')
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
            booking = form.save()

            # Call the mpesa_stk_push view
            mpesa_url = request.build_absolute_uri(
                reverse('transactions:send_stk_push', kwargs={'booking_id': booking.id}))
            payload = {
                'phone_no': phone
            }
            response = requests.post(
                mpesa_url, data=payload, cookies=request.COOKIES)

            event = get_object_or_404(Event, pk=pk)
            if event.slots > 0:
                charge_per_slot = round(event.total_budget_amount / event.slots)
            else:
                charge_per_slot = 0

            context = {
                'event': event,
                'charge_per_slot': charge_per_slot,
                'success_message': "An M-pesa STK push has been inititated on your phone, please complete the transaction..."
            }
            if response.status_code == 200:
                message = f"Hi, {user.username},\nYour reservation for {event.title} have been received and we have initiated payment, kindly complete it.\nThank you.\n\n By Kampus iParty."
                formatted_phone_number = f"+254{booking.user.phone_number[1:]}"
                response = send_whatsapp_message(
                    formatted_phone_number, message, event.title)
                print(response)
                return render(request, 'event_details.html', context)
            
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
