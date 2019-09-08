import json, tweepy, time
from flask import Flask, render_template, Response

app = Flask(__name__)

"""
Get data from config.json
"""
global user
with open('config.json') as config_file:
        data = json.load(config_file)

apiKey = data['consumer']['apiKey']
apiSecretKey = data['consumer']['apiSecretKey']
accessToken = data['tokens']['accessToken']
accessTokenSecret = data['tokens']['accessTokenSecret']
user = data['user']


"""
Defined routes
"""
@app.route('/')
def index():
    return render_template('index.html', value=user.capitalize())

@app.route("/update")
def follower_count():
    return Response(get_followers(), mimetype="text/event-stream")

@app.route("/tweets")
def tweet_count():
    return Response(get_num_tweets(), mimetype="text/event-stream")

@app.route("/likes")
def likes_count():
    return Response(get_num_likes(), mimetype="text/event-stream")

    
"""
Authenticate to twitter
"""
def auth():   
    global api 
    auth = tweepy.OAuthHandler(apiKey, apiSecretKey)
    auth.set_access_token(accessToken, accessTokenSecret)
    api = tweepy.API(auth)

"""
Get/return follower count
"""
def get_followers():
    while True:
        try:
            follower_count = str(api.get_user(user).followers_count)
            yield "data: {}\n\n".format(follower_count)
        except tweepy.RateLimitError:
            print("Followers rate limit reached.")
            time.sleep(15 * 60)

"""
Get/return number of tweets
"""
def get_num_tweets():
    while True:
        try:
            tweet_count = str(api.get_user(user).statuses_count)
            yield "data: Number of combined tweets/retweets: {}\n\n".format(tweet_count)
        except tweepy.RateLimitError:
            print("Tweet count rate limit reached.")
            time.sleep(15 * 60)

"""
Get/return number of liked tweets
"""
def get_num_likes():
    while True:
        try:
            likes_count = str(api.get_user(user).favourites_count)
            yield "data: Total Tweets {} has liked: {}\n\n".format(user, likes_count)
        except tweepy.RateLimitError:
            print("Likes count rate limit reached.")
            time.sleep(15 * 60)


if __name__ == "__main__":
    auth()
    app.run(host='0.0.0.0', threaded=True)