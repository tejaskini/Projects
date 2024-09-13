# Twitter Sentiment Analysis  :
On this Repo created a Twitalytics (Twitter Sentiment Analysis)on python GUI (Tkinter) library.


# Disclaimer :skull_and_crossbones:
I am not provideing twitter **API** keys. You have get twitter API keys on twitter developer account. Get [API Keys](https://developer.twitter.com/)

Get a API key and put in the below code section

```python
def click():  
    user_name = user_value.get()
    hash_name = hash_value.get()
    
    #insert here twitter API keys
    consumerKey = ""
    consumerSecret = ""
    accessToken = ""
    accessTokenSecret = ""
    
    authenticate = tweepy.OAuthHandler(consumerKey, consumerSecret)
    authenticate.set_access_token(accessToken, accessTokenSecret)
    api = tweepy.API(authenticate, wait_on_rate_limit = True) # api object
```
