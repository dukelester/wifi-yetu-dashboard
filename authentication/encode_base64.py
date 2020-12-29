import base64
from . import keys

def generate_password(formarted_time):
    
    # base64 encode
    data_to_encode = keys.business_short_code + keys.lipa_na_mpesa_passkey + formarted_time

    encoded_string = base64.b64encode(data_to_encode.encode())

    decoded_password = encoded_string.decode("utf-8")

    # print(decoded_password)
    return decoded_password