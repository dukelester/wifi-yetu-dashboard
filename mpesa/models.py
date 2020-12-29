from django.db import models


# Create your models here.
class LNMOnline(models.Model):
    merchant_request_id = models.CharField(max_length=20, blank=True, null=True)
    checkout_request_id = models.CharField(max_length=100, blank=True, null=True)
    result_code = models.IntegerField(blank=True, null=True)
    result_description = models.CharField(max_length=200, blank=True)
    saccess_amount = models.FloatField(blank=True, null=True)
    saccess_mpesa_receipt_number = models.CharField(max_length=20, blank=True)
    saccess_transaction_date = models.CharField(max_length=20, blank=True)
    saccess_balance = models.FloatField(max_length=10, blank=True, null=True)
    saccess_phone_number = models.CharField(max_length=15, blank=True, null=True)
    success_result_description = models.CharField(max_length=150, blank=True)
    fail_result_description = models.CharField(max_length=150, blank=True)
    fail_merchant_request_id = models.CharField(max_length=150, blank=True)
    fail_result_code = models.IntegerField(blank=True, null=True)
