import requests

url = "https://api.nasa.gov/planetary/apod"
params = {
    "api_key": "DEMO_KEY",
    "date": "2025-06-10"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error:", response.status_code, response.text)
