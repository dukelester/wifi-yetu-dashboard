from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from mpesa.models import LNMOnline
from .serializers import LNMOnlineSerializer


class LNMCallbackUrlAPIView(CreateAPIView):
    queryset = LNMOnline.objects.all()
    serializer_class = LNMOnlineSerializer
    permission_classes = [AllowAny]

    def create(self, request):
        merchant_request_id = request.data['Body']['stkCallback']['MerchantRequestID']
        checkout_request_id = request.data['Body']['stkCallback']['CheckoutRequestID']
        # print(merchant_request_id)
        # print(checkout_request_id)

        result_code = request.data['Body']['stkCallback']['ResultCode']
        result_description = request.data['Body']['stkCallback']['ResultDesc']
        # print(result_code)
        # print(result_description)

        if result_code == 0:
            saccess_amount = request.data["Body"]["stkCallback"]["CallbackMetadata"]['Item'][0]['Value']
            saccess_mpesa_receipt_number = request.data["Body"]["stkCallback"]["CallbackMetadata"]['Item'][1]['Value']
            saccess_transaction_date = request.data["Body"]["stkCallback"]["CallbackMetadata"]['Item'][3]['Value']
            saccess_balance = ""
            saccess_phone_number = request.data["Body"]["stkCallback"]["CallbackMetadata"]['Item'][4]['Value']
            success_result_description = request.data['Body']['stkCallback']['ResultDesc']

            # do__save()
            saccess_LNMOnline = LNMOnline.objects.create(
                merchant_request_id=merchant_request_id,
                checkout_request_id=checkout_request_id,
                result_code=result_code,
                result_description=result_description,
                saccess_amount=saccess_amount,
                saccess_mpesa_receipt_number=saccess_mpesa_receipt_number,
                saccess_transaction_date=saccess_transaction_date,
                saccess_balance=saccess_balance,
                saccess_phone_number=saccess_phone_number,
                success_result_description=success_result_description,
            )
            saccess_LNMOnline.save()
        else:
            fail_result_description = request.data['Body']['stkCallback']['ResultDesc']
            fail_merchant_request_id = merchant_request_id
            fail_result_code = result_code
            failed_LNMOnline = LNMOnline.objects.create(
                fail_merchant_request_id=merchant_request_id,
                fail_result_code=result_code,
                fail_result_description=fail_result_description,
            )
            failed_LNMOnline.save()
            # do__save()

        return Response({"ResponseDesc": request.data})
