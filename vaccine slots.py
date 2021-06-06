import requests
import json

pincode = input("Enter pincode:")
date = input("Enter date:")

params = {
    'pincode':pincode,
    'date':date
}

url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin"

response = requests.get(url=url, params=params)

data = response.json()

print(json.dumps(data, indent=4))

 