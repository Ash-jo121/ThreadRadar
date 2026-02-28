import json
import requests
import time

HEADERS = {"User-Agent":"ThreadRadar/1.0"}

SUBREDDITS = ["pennystocks","smallstreetbets","RobinHoodPennyStocks"]

def fetch_posts(subreddit,category="hot",limit=25):
    url = f"https://www.reddit.com/r/{subreddit}/{category}.json?limit={limit}"
    response = requests.get(url,headers=HEADERS);

    if response.status_code != 200:
        print(f"Failed to fetch posts from the subreddit: {subreddit} :: {response.status_code}")
        return []
    
    posts = response.json()["data"]["children"];
    result = [];

    print(f"Fetched a total of {len(posts)} posts from the subreddit")

    for post in posts:
        d=post["data"]
        result.append({
            "id":d["id"],
            "title":d["title"],
            "body":d.get("selftext",""),
            "score":d["score"],
            "subreddit":subreddit,
            "url":f"https://www.reddit.com{d["permalink"]}"
        })

    return result


def fetch_comments(post_id,subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/comments/{post_id}.json"
    response = requests.get(url,headers = HEADERS)

    if(response.status_code != 200):
        return []

    comments = []
    try:
        comment_list = response.json()[1]["data"]["children"]
        for c in comment_list:
            if(c["kind"] == "t1"):
                comments.append({
                    "body":c["data"]["body"],
                    "score":c["data"]["score"]
                })
    except:
        pass

    return comments


def fetch_all():
    all_data = []
    for subreddit in SUBREDDITS:
        print(f"Fetching r/{subreddit}...")
        posts = fetch_posts(subreddit)

        for post in posts:
            comments = fetch_comments(post["id"],subreddit)
            post["comments"] = comments
            all_data.append(post)
            time.sleep(1)

        time.sleep(2)

    print(f"Fetched {len(all_data)} posts total")
    return all_data

if __name__=="__main__":
    data = fetch_all()
    print(data[0])