from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Transaction
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
from requests.auth import HTTPBasicAuth
from django.http import HttpResponse
import json
import os
from .mpesa import MpesaAccessToken, LipaNaMpesaPassword
from bookings.models import Booking

class TokenGeneratorView(View):
    def get(self, request, *args, **kwargs):
        consumer_key = os.environ.get('MPESA_CONSUMER_KEY')
        consumer_secret = os.environ.get('MPESA_CONSUMER_SECRET')
        api_URL = 'https://api.safaricom.co.ke/oauth/v1/generate'

        r = requests.get(api_URL, auth=HTTPBasicAuth(
            consumer_key, consumer_secret))

        if r.status_code == 200:
            mpesa_access_token = json.loads(r.text)
            validated_mpesa_access_token = mpesa_access_token["access_token"]

            return JsonResponse({"token": validated_mpesa_access_token})
        else:
            return JsonResponse({"error": "Failed to generate token"}, status=r.status_code)

@csrf_exempt
@login_required
def mpesa_stk_push(request, booking_id):
    if request.method == 'POST':
        user = request.user
        access_token = MpesaAccessToken.validated_mpesa_access_token
        server_url = os.environ.get('SERVER_URL')

        booking = get_object_or_404(Booking, id=booking_id)

        api_url = "https://api.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}

        phone = request.POST.get('phone_no')
        amount = round(booking.event.total_budget_amount / booking.event.slots)
        call_back_url = f"{server_url}/mpesa/mpesa-callback/{user.id}/{booking_id}"

        if phone and amount:
            mpesa = LipaNaMpesaPassword()
            request_payload = {
                "BusinessShortCode": mpesa.business_short_code,
                "Password": mpesa.generate_password(),
                "Timestamp": mpesa.payment_time,
                "TransactionType": "CustomerBuyGoodsOnline",
                "Amount": amount,
                "PartyA": phone,
                "PartyB": mpesa.business_short_code,
                "PhoneNumber": phone,
                "CallBackURL": call_back_url,
                "AccountReference": "Wamae Ndiritu",
                "TransactionDesc": "Web Development Charges"
            }

            response = requests.post(
                api_url, json=request_payload, headers=headers)

            print(response.text)

            return HttpResponse(response.text, content_type='application/json')

        else:
            return JsonResponse({"message": "Invalid request parameters"}, status=400)
    else:
        return JsonResponse({"message": "Method not allowed"}, status=405)

# def handle_mpesa_callback(request, client_id, order_id):
#     data = json.loads(request.body)
#     if request.method == 'POST':
#         # Handle all unsuccessful transactions
#         if data['Body']['stkCallback']['ResultDesc'] != "The service was accepted successfully":
#             async_to_sync(send_message_to_client)(
#                 client_id, {"type": "incomplete_transaction", "response": {"message": data['Body']['stkCallback']['ResultDesc']}})
#             return JsonResponse({"message": "Transaction unsuccessful"}, status=402)

#         callbackMetaData = data['Body']['stkCallback'].get(
#             'CallbackMetadata', None)

#         if callbackMetaData is not None:
#             data = data['Body']['stkCallback']['CallbackMetadata']['Item']

#             # Extract relevant fields
#             amount = data[0].get('Value')
#             receipt_number = data[1].get('Value')
#             balance = data[2].get('Value')
#             transaction_date = data[3].get('Value')
#             phone_number = data[4].get('Value')

#             # GET THER USERNAME
#             user = CustomUser.objects.get(id=client_id)
#             user_full_name = f"{user.first_name} {user.last_name}"
#             order = Order.objects.get(id=order_id)

#             # Create the MpesaTransaction object
#             transaction = MpesaTransaction.objects.create(
#                 amount=amount,
#                 receiptNumber=receipt_number,
#                 balance=balance,
#                 transactionDate=transaction_date,
#                 phoneNumber=phone_number,
#                 fullName=user_full_name,
#                 order_id=order
#             )

#             async_to_sync(send_message_to_client)(
#                 client_id, {"message": "Your transaction has been processed successfully!", "amount": transaction.amount, "ReceiptNumber": transaction.receiptNumber})

#         return Response({"message": "Your transaction has been processed successfully!"}, status=201)
#     return JsonResponse({'message': 'Method not allowed'}, status=405)



def transaction_list(request):
    transactions = Transaction.objects.all()
    context = {'transactions': transactions}
    return render(request, 'transaction_list.html', context)

def transaction_detail(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    context = {'transaction': transaction}
    return render(request, 'transaction_detail.html', context)
