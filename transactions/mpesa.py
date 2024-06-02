import requests
import json
from requests.auth import HTTPBasicAuth
import os
import base64
from datetime import datetime


class MpesaCredential:
    consumer_key = os.environ.get('MPESA_CONSUMER_KEY')
    consumer_secret = os.environ.get('MPESA_CONSUMER_SECRET')
    api_URL = 'https://api.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    pass_key = os.environ.get('MPESA_PASS_KEY')
    business_short_code = os.environ.get('MPESA_BUSINESS_SHORT_CODE')
    till_no = os.environ.get('MPESA_TILL_NO')


class LipaNaMpesaPassword(MpesaCredential):
    """Generates Mpesa Password in the base 64 format"""
    payment_time = datetime.now().strftime('%Y%m%d%H%M%S')
    OffSetValue = '0'

    def generate_password(self):
        """Generate password"""
        data_to_encode = self.business_short_code + self.pass_key + self.payment_time
        online_password_bytes = base64.b64encode(data_to_encode.encode())
        return online_password_bytes.decode('utf-8')


class MpesaAccessToken:
    """Generates mpesa access token"""
    r = requests.get(MpesaCredential.api_URL,
                     auth=HTTPBasicAuth(MpesaCredential.consumer_key, MpesaCredential.consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]
