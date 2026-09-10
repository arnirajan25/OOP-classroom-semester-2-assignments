import requests

url = "https://example.com"

response = requests.get(url)

print("HTTP Status Code:", response.status_code)
