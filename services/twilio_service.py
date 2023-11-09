import os
from twilio.rest import Client

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)


def send_sms(number: str, message: str):
    try:
        message = client.messages.create(
            to=number, from_=TWILIO_PHONE_NUMBER, body=message
        )
        print(message.sid)

    except Exception as e:
        print(e)


def send_bulk_sms(numbers_list: list[str], body: str):
    try:
        print("=== Starting bulk messaging ===")
        for number in numbers_list:
            print("Sending to " + number)
            message = client.messages.create(
                to=number, from_=TWILIO_PHONE_NUMBER, body=body
            )
            print(message)

        print("=== Ending bulk messaging ===")

    except Exception as err:
        print(err)
        return
