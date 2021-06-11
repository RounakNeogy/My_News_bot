# My_News_bot
## Introduction
This is a telegram news bot which can fetch the top 5 news about any location, language and topic specified.
## About Bot
- It is a python-Flask application 
- It uses gnewsclient to fetch news
- It is trained using dialogflow
- It provides a custom keyboard with the news topics for the ease of the user
- It is deployed using Heroku 
## Code snipet
This is the code to fetch news from gnewsclient with specific language, location, and topic
```python
client = gnewsclient.NewsClient()
def fetch_news(parameters):
    client.language=parameters.get('language')
    client.location=parameters.get('geo-country')
    client.topic=parameters.get('topic')

    return client.get_news()
```

## Demo

# Tech-Stack


