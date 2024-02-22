import requests
from send_email import send_email

topic = "topic"
api_key = "api_key"
url = (f"https://newsapi.org/v2/everything?"
       f"q={topic}&"
       f"sortBy=publishedAt&"
       f"apiKey={api_key}&"
       f"language=en")

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

message = "Subject: Today's news" + "\n"

# Access the article titles and descriptions
for article in content["articles"][:20]:
    if article['title'] and article['description'] is not None:
        message += "Title: " + article['title'].replace('\n', '\\n') + "\n" \
                   + "Description: " + article['description'].replace('\n', '\\n') + "\n" \
                   + "Link: " + article['url'] + 2 * "\n"

send_email(message.encode('utf-8'))
