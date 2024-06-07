import requests
import json
query = input("Which news do you wanna know about? ")
# source = input("Which source you wanna know from? ")
api_key = input("Enter Your API key: ")
url = (f"https://newsapi.org/v2/everything?q={query}&from=2024-02-29&sortBy=publishedAt&apiKey=bd9dae65e60f4a25b8f9a231b2d88e93")
r = requests.get(url)
news = json.loads(r.text)
for article in news["articles"]:
    print(article["title"]) 
    print(article["description"])
    print("------------------------------------")
