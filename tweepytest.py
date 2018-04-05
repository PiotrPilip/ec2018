import tweepy
from configparser import ConfigParser as ConfPar
from trackNames import trackNames
config = ConfPar()
config.read('main.conf')

consumer_key=config['TWEEPY']['consumer_key']
consumer_secret=config['TWEEPY']['consumer_secret']
access_token=config['TWEEPY']['access_token']
access_token_secret=config['TWEEPY']['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):
    

    def on_status(self, status):
        dic= {}
        dic['tweetID'] = status.id_str
        dic['userID'] = status.user.id_str
        dic['userName']= status.user.name
        dic['location']=status.user.location
        dic['timeZone']=status.user.time_zone
        dic['createTime']=status.created_at
        
        print(dic)
        exit()
        

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(track=trackNames)
        
