# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# # Register your models here.
# from mpesa_api.models import MpesaPayment, BaseModel, MpesaCalls, MpesaCallBacks
# from serverresponse.models import LMNOnline
# from authentication.models import AuthProfile, AuthPayments

# portal models
# from wifiyetu.models import Profile, Payments
#
# admin.site.register(Profile)
# admin.site.register(Payments)
#
#
# # server response models
#
# class LMNOnlineAdmin(admin.ModelAdmin):
#     list_display = ('Phonenumber', 'A_mmount', 'Transactiondate', 'Resultdesc')
#

# admin.site.register(LMNOnline, LMNOnlineAdmin)


# authentication models

# class AuthProfiles(admin.ModelAdmin):
#     list_display = ('AuthProfile.user', 'name', 'phoneno')


# admin.site.register(AuthProfile)


# class AuthPaymentss(admin.ModelAdmin):
#     list_display = ('AuthProfile.user', 'name', 'phone')


# admin.site.register(AuthPayments)

# mpesa api models
# admin.site.register(BaseModel)

# M-pesa Payment models

# admin.site.register(MpesaCalls)
# admin.site.register(MpesaCallBacks)
# admin.site.register(MpesaPayment)
# from mpesa.models import PaymentTransaction, Wallet
#
#
# class PaymentTransactionAdmin(admin.ModelAdmin):
#     list_display = ("phone_number", "amount", "isFinished",
#                     "isSuccessFull", "trans_id", 'date_created', 'date_modified')
#
#
# admin.site.register(PaymentTransaction, PaymentTransactionAdmin)
# admin.site.register(Wallet)
