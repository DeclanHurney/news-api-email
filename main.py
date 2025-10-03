import requests
from dotenv import load_dotenv
import os

from send_email import send_email

load_dotenv()   #1) Parse a .env file and then load all the variables found as environment variables
news_org_api_key = os.getenv('NEWS_ORG_API_KEY')
subject = os.getenv('SUBJECT')

# All parameters that can be added to the URL are here: https://newsapi.org/docs/endpoints/everything
url=("https://newsapi.org/v2/everything?"
     "q="+subject+""
                  "&sortBy=publishedAt"
                  "&language=en"
                  "&apiKey="+news_org_api_key)
print(url)
request = requests.get(url)
content = request.json()
# Access the article titles and description
body = ""
for index, article in enumerate(content["articles"][:20]):
    if article["title"] is not None:
        body = body + (f"Subject: Today's News\n"         
                       f"Article"
                       f" {index+1}\nTitle: "
                       f"{article["title"]}\nDescription: "
                       f"{article['description']}\nURL: "
                       f"{article['url']}")+2*"\n"

body = body.encode("utf8")

print(body)
send_email(body)


# 1) Find an image on a web site
# 2) right click on it and choose Open Image in a new tab. Copy the link into the
# following variable
# 3) url = "https://www.connachtrugby.ie/storage/images/Galway%20Bay%20FM.svg"
# 4) import requests
# 5) response = requests.get(url)
# 6) response.content would return the bytes which form part of this image. We
# need these bytes to be saved into an image.jpg file in write binary mode on
# our own filesystem
# 7) with open('image.jpg', 'wb') as file:
#     file.write(response.content)
# 8) image.jpg should appear on filesystem


url = "https://www.connachtrugby.ie/storage/images/Galway%20Bay%20FM.svg"
response = requests.get(url)
with open('image.jpg', 'wb') as file:
    file.write(response.content)