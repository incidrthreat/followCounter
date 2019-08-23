import json, tweepy

from flask import Flask



def init():
    global api
    """
    Get api token and keys from config.json
    """
    with open('config.json') as config_file:
        data = json.load(config_file)

    apiKey = data['consumer']['apiKey']
    apiSecretKey = data['consumer']['apiSecretKey']
    accessToken = data['tokens']['accessToken']
    accessTokenSecret = data['tokens']['accessTokenSecret']
    
    auth = tweepy.OAuthHandler(apiKey, apiSecretKey)
    auth.set_access_token(accessToken, accessTokenSecret)
    api = tweepy.API(auth)

def get_followers():
    return api.get_user('hackmethod').followers_count

def main():    
    print(get_followers())
    
    

if __name__ == "__main__":
    init()
    main()