

import requests

from api_key import apiKey

query = input("What type of news are you interested in today? ")

url = f"https://newsapi.org/v2/everything?q={query}=2025-05-25&to=2025-05-25&sortBy=popularity&apiKey={apiKey}"

getData = requests.get(url).json()

articles = getData["articles"]

for index, article in enumerate(articles):
    print(index + 1, article["title"], article["url"])
    print("\n ****************************** \n")

