# from django.test import TestCase

# # Create your tests here.
# # Download the helper library from https://www.twilio.com/docs/python/install
# import os
# from twilio.rest import Client

# # Set environment variables for your credentials
# # Read more at http://twil.io/secure
# account_sid = "ACb8294d077aa1eaf72d83d13da29ebe79"
# auth_token = '6a22b3406f24c6c285d225a226ff0498'
# verify_sid = "VAde484e68d149cba0e2a5ac7ad7d638a8"
# verified_number = "+919170539408"

# client = Client(account_sid, auth_token)

# verification = client.verify.v2.services(verify_sid) \
#   .verifications \
#   .create(to=verified_number, channel="sms")
# print(verification.status)

# otp_code = input("Please enter the OTP:")

# verification_check = client.verify.v2.services(verify_sid) \
#   .verification_checks \
#   .create(to=verified_number, code=otp_code)
# print(verification_check.status)
from django.contrib.auth.models import User
from app.models import *
d = {'type': 'websocket', 'path': '/ws/8/', 'raw_path': b'/ws/8/', 'headers': [(b'host', b'localhost:8000'), (b'connection', b'Upgrade'), 
                                                                               (b'pragma', b'no-cache'), (b'cache-control', b'no-cache'), 
                                                                               (b'user-agent', b'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'), 
                                                                               (b'upgrade', b'websocket'), (b'origin', b'http://localhost:8000'), (b'sec-websocket-version', b'13'), 
                                                                               (b'accept-encoding', b'gzip, deflate, br'), (b'accept-language', b'en-GB,en-US;q=0.9,en;q=0.8'), 
                                                                               (b'cookie', b'user=9170539408; verified=True; csrftoken=XncbTH3eROBPIRiSBL3qrTN98Zs9v9Mn; sessionid=rl84mx2a3s0r4blgfcmmikbi5riyxd2y'), 
                                                                               (b'authorization', b'JWT qyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc0MTE2NDIzLCJqdGkiOiJjZmVhY2EwZTk3NDE0NzNhODE0YjhmODE1M2EyMGMxYiIsInVzZXJfaWQiOjF9.Uh4vJmTNxuVMC3_IsrapQrD5DWsvrNkitsj9i_ejH6E'), 
                                                                               (b'sec-websocket-key', b'y/THholg8tk9L2PdNJ54KQ=='), (b'sec-websocket-extensions', b'permessage-deflate; client_max_window_bits')], 
      'query_string': b'', 
     'client': ['127.0.0.1', 35412], 'server': ['127.0.0.1', 8000], 'subprotocols': [], 'asgi': {'version': '3.0'}, 
     'cookies': {'user': '9170539408', 'verified': 'True', 'csrftoken': 'XncbTH3eROBPIRiSBL3qrTN98Zs9v9Mn', 
                 'sessionid': 'rl84mx2a3s0r4blgfcmmikbi5riyxd2y'}, 
     'session': '<django.utils.functional.LazyObject object at 0x7f9a806babb0>', 
     'user': '<channels.auth.UserLazyObject object at 0x7f9a806cb4c0>', 'path_remaining': '', 
     'url_route': {'args': (), 'kwargs': {'id': 8}}}

print(d['cookies']['user'])
print(User.objects.get(id=8))