# -*- encoding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class PaymentRequestHeaders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # hostel_name = models.ForeignKey(LandlordProfile, on_delete=models.CASCADE)
    merchant_request_id = models.CharField(max_length=100)
    checkout_request_id = models.CharField(max_length=100)
    response_description = models.CharField(max_length=100)
    phone_number_used_for_payment = models.CharField(max_length=100, blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} request was {self.response_description}: checkout id = {self.checkout_request_id}'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    your_full_name = models.CharField(max_length=191, blank=True, null=True)
    phone_number = models.CharField(max_length=191, blank=True, null=True)
    user_picture = models.ImageField(upload_to='tenant_profile')
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.your_full_name} : {self.phone_number} Profile'
