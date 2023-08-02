from django.http import JsonResponse
import json
import requests


def sanboxpayment(request):
    access_token = "Your Access Token"
    if access_token:
        url = "https://api.sandbox.paypal.com/v1/payments/payouts"

        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json",
        }

        data = {
            "sender_batch_header": {
                "email_subject": "You received a payment!",
                "recipient_type": "EMAIL"
            },
            "items": [
                {
                    "recipient_type": "EMAIL",  # choose one type
                    "amount": {
                        "value": "15.00",
                        "currency": "USD"
                    },
                    "receiver": "@gmail.com",
                    "note": "sending message......",
                    "sender_item_id": "item_2",
                }
            ]
        }

        try:
            # Encode the data as JSON
            data_json = json.dumps(data).encode('utf-8')

            # Make the POST request using Django's HttpRequest
            req = requests.post(url, data=data_json, headers=headers)

            # You can parse the JSON data from the response
            response_json = req.json()

            # Return the response data as JSON
            return JsonResponse(response_json)
        except requests.RequestException as e:
            return JsonResponse({"error": "An error occurred: {}".format(e)}, status=500)
    else:
        return JsonResponse({"error": "Failed to get access token."}, status=500)
