import requests
from dotenv import load_dotenv
import os

from send_email import send_email

load_dotenv()   #1) Parse a .env file and then load all the variables found as environment variables
news_org_api_key = os.getenv('NEWS_ORG_API_KEY')
subject = os.getenv('SUBJECT')

url=("https://newsapi.org/v2/everything?q="+subject+"&sortBy=publishedAt&apiKey"
     "="+news_org_api_key)
print(url)
request = requests.get(url)
content = request.json()
# Access the article titles and description
body = ""
for index, article in enumerate(content["articles"]):
    if article["title"] is not None:
        body = body + f"Article {index}\nTitle: {article["title"]}\nDescription: {article['description']}"+2*"\n"

body = body.encode("utf8")

print(body)
send_email(body)


