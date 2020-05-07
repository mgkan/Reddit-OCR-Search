import praw
from pytesseract import image_to_string
import requests
import io
from PIL import Image
from fuzzywuzzy import fuzz

reddit = praw.Reddit(Auth)

sub_input = input("subreddit: ")
post_input = input("post: ")

sub = reddit.subreddit(sub_input)
hot_sub = sub.hot(limit = 200)

imgs = []
results = []

for post in hot_sub:
    if not post.stickied:
        url = post.url
        imgs.append(url)


for link in imgs:
    
    response = requests.get("{}".format(link))
    img = Image.open(io.BytesIO(response.content))
    ratio = fuzz.ratio(post_input.lower(), image_to_string(img).lower())
   
    if ratio >= 50:
        results.append(link)
    

print(results)
print(imgs)

