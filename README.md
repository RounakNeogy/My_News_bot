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
## News-Topic 
This are the topics provides by gnewsclient
- Top Stories
- World
- Nation
- Business
- Technology
- Entertainment
- Sports
- Science
- Health

## Demo
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/HMXuAT4HIfY/0.jpg)](https://www.youtube.com/watch?v=HMXuAT4HIfY)

# Tech-Stack
<a href="https://python.org/" title="python"><img src="https://github.com/get-icon/geticon/raw/master/icons/python.svg" alt="python" width="40px" height="40px"></a>
<a href="https://dialogflow.cloud.google.com/" title="dialogflow"><img src="https://github.com/get-icon/geticon/raw/master/icons/dialogflow.svg" alt="dialogflow" width="40px" height="40px"></a>
<a href="https://flask.com/" title="python"><img src="https://github.com/get-icon/geticon/raw/master/icons/flask.svg" alt="flask" width="40px" height="40px"></a>
<a href="https://heroku.com/" title="python"><img src="https://github.com/get-icon/geticon/raw/master/icons/heroku.svg" alt="heroku" width="40px" height="40px"></a>
# Try is out
Search for @Rounak26_bot in Telegram, hopefully it will work.
