import requests
import os
import json
from dotenv import load_dotenv

# load username/password from .env file
load_dotenv()
user = os.getenv("PELOTON_USER")
password = os.getenv("PELOTON_PASSWORD")

# start session by logging in
s = requests.Session()
payload = {'username_or_email': user, 'password': password}
s.post('https://api.onepeloton.com/auth/login', json=payload)

# get my profile data
response = s.get('https://api.onepeloton.com/api/me')

if response.status_code != 200:
    print('Something has gone wrong, try again')
else:
    json_data = json.loads(response.text)
    print(json_data)
