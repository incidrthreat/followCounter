import json, tweepy, string

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    auth()
    return "{} has {} followers!".format(user.capitalize(), str(get_followers()))

    
"""
Get data from config.json
"""
def auth():
    global api, user
    with open('config.json') as config_file:
        data = json.load(config_file)

    apiKey = data['consumer']['apiKey']
    apiSecretKey = data['consumer']['apiSecretKey']
    accessToken = data['tokens']['accessToken']
    accessTokenSecret = data['tokens']['accessTokenSecret']
    user = data['user']
    
    auth = tweepy.OAuthHandler(apiKey, apiSecretKey)
    auth.set_access_token(accessToken, accessTokenSecret)
    api = tweepy.API(auth)

"""
Get/return follower count
"""
def get_followers():
    return api.get_user(user).followers_count
    

if __name__ == "__main__":
    app.run()