import requests
import os
from datetime import datetime

from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://fcm.googleapis.com/fcm/send"
# ? Get from FCM dashboard
SERVER_KEY = os.environ.get("SERVER_KEY")
# ? Get from client
RECEIVER = os.environ.get("RECEIVER")


def send_notif_example():
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"key={SERVER_KEY}"
    }

    data = {
        "to": RECEIVER,
        "data": {
            "content": "Test push notification success!",
            "created_date": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "url": "https://google.com",
            "img_link": "",
        }
    }

    response = requests.post(BASE_URL, headers=headers, json=data)

    print(response.status_code)
    print(response.text)
    if response.status_code == 200:
        print("Send notif successfully")
    else:
        print("Something's wrong")

def send_multiple_notif_example():
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"key={SERVER_KEY}"
    }

    data = {
        "registration_ids": [RECEIVER],
        "data": {
            "content": "Test push notification success!",
            "created_date": datetime.now(),
            "url": "https://google.com",
            "img_link": "",
        }
    }

    response = requests.post(BASE_URL, headers=headers, json=data)

    print(response.status_code)
    print(response.text)
    if response.status_code == 200:
        print("Send notif successfully")
    else:
        print("Something's wrong")


send_notif_example()
# send_multiple_notif_example()
