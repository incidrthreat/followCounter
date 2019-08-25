import json, tweepy, time

from flask import Flask, render_template, Response, json

app = Flask(__name__)

global user, socketKey
with open('config.json') as config_file:
        data = json.load(config_file)

apiKey = data['consumer']['apiKey']
apiSecretKey = data['consumer']['apiSecretKey']
accessToken = data['tokens']['accessToken']
accessTokenSecret = data['tokens']['accessTokenSecret']
user = data['user']

@app.route('/')
def index():
    return render_template('index.html', value=user.capitalize())

@app.route("/update")
def send_count():
    return Response(get_followers(), mimetype="text/event-stream")

    
"""
Get data from config.json
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
            print("Rate Limit Error")
            time.sleep(15 * 60)


if __name__ == "__main__":
    auth()
    app.run(host='0.0.0.0', threaded=True)