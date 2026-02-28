import requests

headers = {"User-Agent": "ThreadRadar/1.0"}

response = requests.get(
    "https://www.reddit.com/r/pennystocks/hot.json?limit=10",
    headers=headers
)

data = response.json()
posts = data["data"]["children"]

for post in posts:
    print(post["data"]["title"], "| Score:", post["data"]["score"])