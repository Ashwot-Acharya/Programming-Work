import requests
import json

url=''
response= requests.get(url)

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

print(response.json())
