# -*- encoding: utf-8 -*-
import json

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.sites import requests
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django.http import HttpResponse
from django.urls import reverse

from mpesa.models import LNMOnline
from . import keys
from .access_token import generate_access_token
from .encode_base64 import generate_password
from .forms import LoginForm, SignUpForm, PaymentForm
from .models import PaymentRequestHeaders
from django.contrib import messages, auth


def login_view(request):
    # form = LoginForm(request.POST or None)
    #
    # msg = None
    #
    # if request.method == "POST":
    #
    #     if form.is_valid():
    #         username = form.cleaned_data.get("username")
    #         password = form.cleaned_data.get("password")
    #         user = authenticate(username=username, password=password)
    #         if user is not None:
    #
    #             login(request, user)
    #             return redirect("/dashboard/")
    #         else:
    #             # msg = 'Invalid credentials'
    #             messages.success(request, 'invalid credentials!')
    #             return render(request, "accounts/login.html", {"form": form})
    #     else:
    #         msg = 'Error validating the form'
    #
    #         return render(request, "accounts/login.html", {"form": form, "msg": msg})
    #
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(email,password)

        user =auth.authenticate( username = email, password = password)
        print(user)

        if user is not None:
            login(request, user)
            return redirect('/')


        else:

            messages.warning(request, 'Incorrect username/password!')

            return render(request, 'sign-in.html')



    else:

        return render(request,'sign-in.html')




def user_registration(request):
    # msg = None
    # success = False
    #
    # if request.method == "POST":
    #     form = SignUpForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         username = form.cleaned_data.get("username")
    #         raw_password = form.cleaned_data.get("password1")
    #         user = authenticate(username=username, password=raw_password)
    #
    #         # msg = 'User created - please <a href="/login">login</a>.'
    #         # success = True
    #         messages.success(request, 'Account created sucessfully!')
    #
    #         return redirect("/login/")
    #
    #     else:
    #         # msg = 'Form is not valid'
    #         messages.error(request, 'invalid details')
    #
    # else:
    #     form = SignUpForm()
    #
    # return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})
    if request.method == "POST":

        email = request.POST['email']

        password = request.POST['password']
        confirm_password=request.POST['password2']



        if User.objects.filter(email=email).exists():

            messages.warning(request, 'Email exists!')



            return render(request,'register.html')





        # else:

            # if Profile.objects.filter(phoneno=phoneno).exists():
            #     print('phone exists')
            #     messages.warning(request, 'Phone number exists!')
            #     return render(request, 'register.html')
    #
        else:
            if password!= confirm_password:
                messages.warning(request, 'passwords do not match!')
                return render(request, 'sign-up.html')

            else:


                user = User.objects.create_user(email=email, username=email, password=password
                                                )
                user.save()
                messages.success(request, 'Account created sucessfully!')

                return redirect('authlogin')


    else:

        return render(request,'sign-up.html')




def timestamp_convertion():
    pass



def google_login(request):
    redirect_url = "%s://%s%s" % (
        request.scheme, request.get_host(), reverse('google_login')
    )
    if ('code' in request.GET):
        params = {
            'grant_type': 'authorization_code',
            'code': request.GET.get('code'),
            'redirect_uri': redirect_url,
            'client_id': settings.GP_CLIENT_ID,
            'client_secret': settings.GP_CLIENT_SECRET
        }
        url = 'https://accounts.google.com/o/oauth2/token'
        response = requests.post(url, data=params)
        url = 'https://www.googleapis.com/oauth2/v1/userinfo'
        access_token = response.json().get('access_token')
        response = requests.get(url, params={'access_token': access_token})
        user_data = response.json()
        email = user_data.get('email')

        if email:
            user, _ = User.objects.get_or_create(email=email, username=email)
            gender = user_data.get('gender', '').lower()
            if gender == 'male':
                gender = 'M'
            elif gender == 'female':
                gender = 'F'
            else:
                gender = 'O'
            data = {
                'first_name': user_data.get('name', '').split()[0],
                'last_name': user_data.get('family_name'),
                'google_avatar': user_data.get('picture'),
                'gender': gender,
                'is_active': True
            }
            user.__dict__.update(data)
            user.save()
            user.backend = settings.AUTHENTICATION_BACKENDS[0]
            login(request, user)
        else:
            messages.error(
                request,
                'Unable to login with Gmail Please try again'
            )
        return redirect('/')
    else:
        url = "https://accounts.google.com/o/oauth2/auth?client_id=%s&response_type=code&scope=%s&redirect_uri=%s&state=google"
        scope = [
            "https://www.googleapis.com/auth/userinfo.profile",
            "https://www.googleapis.com/auth/userinfo.email"
        ]
        scope = " ".join(scope)
        url = url % (settings.GP_CLIENT_ID, scope, redirect_url)
        return redirect(url)



@login_required(login_url='/user/')
def payments(request):
    context = {}

    if request.user.is_authenticated:
        print('')

    if request.method == 'POST':
        form = PaymentForm(request.POST)

        context['form'] = form

        if form.is_valid():
            phone_number = form.cleaned_data.get('phone_number')
            user_id = form.cleaned_data.get('user_id')
            # time formatting
            formarted_time = timestamp_convertion()
            # to be implemented on production scale
            business_short_code = request.POST['business_short_code']

            hostel_name = request.POST['hostel_name_id']
            amount_payable = request.POST['amount']

            # base64 encode
            decoded_password = generate_password(formarted_time)
            access_token = generate_access_token()
            api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
            headers = {"Authorization": "Bearer %s" % access_token}
            request = {
                "BusinessShortCode": keys.business_short_code,
                "Password": decoded_password,
                "Timestamp": formarted_time,
                "TransactionType": "CustomerBuyGoodsOnline",  # CustomerPayBillOnline
                "Amount": amount_payable,
                "PartyA": phone_number,
                "PartyB": keys.business_short_code,
                "PhoneNumber": phone_number,
                "CallBackURL": "https://accomodations.herokuapp.com/api/payments/lnm/",
                "AccountReference": "Test004Clinton",
                "TransactionDesc": "Rent pay"
            }

            response = requests.post(api_url, json=request, headers=headers)

            mystr = response.text
            obbstr = json.loads(mystr)
            merchant_request_id = obbstr['MerchantRequestID']
            checkout_request_id = obbstr['CheckoutRequestID']
            response_description = obbstr['ResponseDescription']

            payment_request_headers = PaymentRequestHeaders.objects.create(
                merchant_request_id=merchant_request_id,
                checkout_request_id=checkout_request_id,
                response_description=response_description,
                user_id=user_id,
                hostel_name_id=hostel_name,
                phone_number_used_for_payment=phone_number,
            )

            context['checkout_request_id'] = checkout_request_id
            context['response_description'] = response_description
            payment_request_headers.save()

            return redirect('/user/payments/')

    return render(request, 'pay.html', context)


@login_required(login_url='/user/')
def all_user_transaction(request):
    context = {}
    if request.user.is_authenticated:
        previous_transaction = PaymentRequestHeaders.objects.filter(
            user=request.user.id)
        lnmponline = LNMOnline.objects.all()
        context['lnmponline'] = lnmponline
        context['previous_transaction'] = previous_transaction

    return render(request, 'transactions.html', context)


def password_reset(request):
    return render(request, 'password_reset_form.html')


def password_reset_done(request):
    return render(request, 'password_reset_done.html')


def password_reset_confirm(request):
    return render(request, 'password_reset_confirm.html')


def password_reset_complete(request):
    return render(request, 'password_reset_complete.html')
