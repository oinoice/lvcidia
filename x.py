import requests
import json
import os

# URL
url = "https://backend.prd.lvcidia.web3.uken.com/api/tokens/stake"

# Headers
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0",
    "Accept": "application/json",
    "Accept-Language": "en-US,en;q=0.5",
    "Content-Type": "application/json",
    "Authorization": f"Bearer {os.environ.get('LVCIDIA_TOKEN')}",
    # Removing the browser-specific headers like 'Sec-Fetch-*'
}

# Payload
payload = {
    "tokens": [
        {
            "id": 10119,
            "address": "0x10cdcb5a80e888ec9e9154439e86b911f684da7b"
        }
    ],
    "resourceFieldId": 11,
    "lockupPeriod": "LOW"
}

response = requests.post(url, headers=headers, data=json.dumps(payload))

if response.status_code != 201:
    print("Failed to stake tokens!")
    print(response.status_code)
    print(response.text)
else:
    print("Successfully staked tokens!")
