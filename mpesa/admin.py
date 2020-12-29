from django.contrib import admin
from .models import LNMOnline
# Register your models here.


# admin.site.register(LNMOnline)

class LNMOnlineModelAdmin(admin.ModelAdmin):
    list_display = ["saccess_phone_number","saccess_mpesa_receipt_number","saccess_amount","fail_result_description","success_result_description","merchant_request_id","checkout_request_id","result_code","fail_result_code"]
    list_display_links = ["merchant_request_id"]
    list_filter = ["merchant_request_id", "saccess_phone_number"]
    search_fields = ["saccess_phone_number","merchant_request_id"]
    class Meta:
        model = LNMOnline

admin.site.register(LNMOnline, LNMOnlineModelAdmin)