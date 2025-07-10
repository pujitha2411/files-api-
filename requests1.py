import pandas as pd
import requests

url = "https://github.com/ShivamJoker/sample-songs/blob/master/data.json"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    print(df.head())
else:
    print("Failed to fetch data:", response.status_code)
