import re

from django.contrib import messages
from django.http import HttpResponse, JsonResponse
import requests
from django.shortcuts import redirect, render
from requests.auth import HTTPBasicAuth
import json
from . mpesa_credentials import MpesaAccessToken, LipanaMpesaPpassword
from django.views.decorators.csrf import csrf_exempt
from .models import MpesaPayment
from django.http import request
def getAccessToken(request):
    consumer_key = '4ZgVUXcDfeAUT6wDqCKP0K8zxCEETQcY'
    consumer_secret = 'WlnE77VQMT6ur4rQ'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']
    return HttpResponse(validated_mpesa_access_token)

def lipa_na_mpesa_online(request):
    if request.method== 'POST':
        amount=request.POST['amount']
        phone_number=request.POST['phone_number']
        print(phone_number,amount,'ammount')
        if len(phone_number) != 12:
            messages.error(request, "Phone Number too short or too long!")
            return redirect('/')

        else:

            result = re.match('^[254]+$', phone_number[0:3])
            print(result)

            if result == None:
                messages.error(request, "Number did not start with 254")

                return redirect('/')



            else:

                if phone_number.isnumeric() == True:
                    print("got it!")



                    def lipa_na_mpesa():
                        # INPUT VALIDATION

                        access_token = MpesaAccessToken.validated_mpesa_access_token
                        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
                        headers = {"Authorization": "Bearer %s" % access_token}
                        request = {
                            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
                            "Password": LipanaMpesaPpassword.decode_password,
                            "Timestamp":LipanaMpesaPpassword.lipa_time,
                            "TransactionType": "CustomerPayBillOnline",
                            "Amount": amount,
                            "PartyA": phone_number,
                            "PartyB":  LipanaMpesaPpassword.Business_short_code,
                            "PhoneNumber": phone_number,
                            "CallBackURL": "https://firefly-m.herokuapp.com/api/payments/lnm/",
                            "AccountReference": "Duke Lester",
                            "TransactionDesc": "Testing"
                        }

                        response = requests.post(api_url, json=request, headers=headers)

                        print(response.text)


                    lipa_na_mpesa()
                    messages.success(request, "Sucessful. Please check your phone")
                    # save transactions here

                    return redirect('/')

                else:
                    messages.error(request, "Phone Number is not numeric")

                    return redirect('/')




        #
        #
        # access_token = MpesaAccessToken.validated_mpesa_access_token
        # api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        # headers = {"Authorization": "Bearer %s" % access_token}
        # request = {
        #     "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
        #     "Password": LipanaMpesaPpassword.decode_password,
        #     "Timestamp": LipanaMpesaPpassword.lipa_time,
        #     "TransactionType": "CustomerPayBillOnline",
        #     "Amount": 1,
        #     "PartyA": 254799443070,  # replace with your phone number to get stk push
        #     "PartyB": LipanaMpesaPpassword.Business_short_code,
        #     "PhoneNumber": 254799443070,  # replace with your phone number to get stk push
        #     "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
        #     "AccountReference": "Duke Nyamongo",
        #     "TransactionDesc": "Confirm to pay Lester Softwares"
        # }
        # response = requests.post(api_url, json=request, headers=headers)


@csrf_exempt
def register_urls(request):

    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % access_token}
    # Business_short_code
    options = {"ShortCode": LipanaMpesaPpassword.Test_c2b_shortcode,
               "ResponseType": "Completed",
               "ConfirmationURL": "http://127.0.0.1:8000/api/v1/c2b/confirmation",
               "ValidationURL": " http://127.0.0.1:8000/api/v1/c2b/validation"}
    response = requests.post(api_url, json=options, headers=headers)
    return HttpResponse(response.text)

@csrf_exempt
def call_back(request):
    pass
@csrf_exempt
def validation(request):
    context = {
        "ResultCode": 0,
        "ResultDesc": "Accepted"
    }
    return JsonResponse(dict(context))
@csrf_exempt
def confirmation(request):

    mpesa_body =request.body.decode('utf-8')
    mpesa_payment = json.loads(mpesa_body)
    payment = MpesaPayment(
        first_name=mpesa_payment['FirstName'],
        last_name=mpesa_payment['LastName'],
        middle_name=mpesa_payment['MiddleName'],
        description=mpesa_payment['TransID'],
        phone_number=mpesa_payment['MSISDN'],
        amount=mpesa_payment['TransAmount'],
        reference=mpesa_payment['BillRefNumber'],
        organization_balance=mpesa_payment['OrgAccountBalance'],
        type=mpesa_payment['TransactionType'],
    )
    payment.save()
    context = {
        "ResultCode": 0,
        "ResultDesc": "Accepted"
    }
    return JsonResponse(dict(context))