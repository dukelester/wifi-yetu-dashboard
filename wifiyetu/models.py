# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
#
# from django.contrib.auth.models import User
# from django.db import models
#
#
# # Create your models here.
#
# # mpesa api models
# # from authentication.models import AuthProfile
#
#
# class BaseModel(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         def __str__(self):
#             return self.created_at
#
#
# # M-pesa Payment models
#
# class MpesaCalls(BaseModel):
#     ip_address = models.TextField()
#     caller = models.TextField()
#     conversation_id = models.TextField()
#     content = models.TextField()
#
#     class Meta:
#         verbose_name = 'Mpesa Call'
#         verbose_name_plural = 'Mpesa Calls'
#
#
# class MpesaCallBacks(BaseModel):
#     ip_address = models.TextField()
#     caller = models.TextField()
#     conversation_id = models.TextField()
#     content = models.TextField()
#
#     class Meta:
#         verbose_name = 'Mpesa Call Back'
#         verbose_name_plural = 'Mpesa Call Backs'
#
#
# class MpesaPayment(BaseModel):
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     description = models.TextField()
#     type = models.TextField()
#     reference = models.TextField()
#     first_name = models.CharField(max_length=100)
#     middle_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     phone_number = models.TextField()
#     organization_balance = models.DecimalField(max_digits=10, decimal_places=2)
#
#     class Meta:
#         verbose_name = 'Mpesa Payment'
#         verbose_name_plural = 'Mpesa Payments'
#
#     def __str__(self):
#         return self.first_name
#
#
# # portal models
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     fullname = models.CharField(max_length=100)
#     phone = models.CharField(max_length=15)
#
#
# class Payments(models.Model):
#     name = models.CharField(max_length=100)
#     phone = models.CharField(max_length=15)
#
#
# # server response models
# class LMNOnline(models.Model):
#     Merchant_requestID = models.CharField(max_length=50)
#     # Checkout_requestID=models.CharField(max_length=40)
#     Resultcode = models.IntegerField()
#     Resultdesc = models.CharField(max_length=120)
#     A_mmount = models.FloatField()
#     Mpesa_receiptnumber = models.CharField(max_length=20)
#     Transactiondate = models.DateTimeField()
#     Phonenumber = models.CharField(max_length=13)
#
#     def __str__(self):
#         return f"{self.Phonenumber} has sent  {self.A_mmount} at {self.Transactiondate}"


# authentication models
#
# class AuthProfile(models.Model):
#     AuthProfile.user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
#     name = models.CharField(max_length=256)
#     sex = models.CharField(max_length=256)
#     age = models.CharField(max_length=256, null=True)
#     phoneno = models.CharField(max_length=256)
#     birthday = models.DateField()
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name_plural = "User Profile"


# class AuthPayments(models.Model):
#     AuthProfile.user = models.ForeignKey(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     phone = models.CharField(max_length=15)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name_plural = "User Payments"
