import tweepy
from multiprocessing import Process
from configparser import ConfigParser as ConfPar
from trackNames import trackNames

def loadTwitterKeysFromConfig():
    config = ConfPar()
    config.read('../../main.conf')
    consumer_key=config['TWEEPY']['consumer_key']
    consumer_secret=config['TWEEPY']['consumer_secret']
    access_token=config['TWEEPY']['access_token']
    access_token_secret=config['TWEEPY']['access_token_secret']
    return [consumer_key,consumer_secret,access_token,access_token_secret]

def getTwitterApi(twitterKeys = loadTwitterKeysFromConfig()):
    auth = tweepy.OAuthHandler(twitterKeys[0], twitterKeys[1])
    auth.set_access_token(twitterKeys[2],twitterKeys[3])
    api = tweepy.API(auth)
    return api

def getStreamListener(twitterApi):
    streamListener = TwitterStreamProcessor()
    twitterStream = tweepy.Stream(auth = twitterApi.auth, listener=streamListener)
    return twitterStream

def startStreaming():
    api=getTwitterApi()
    twitterStream=getStreamListener(api)
    twitterStream.filter(track=trackNames)
    
class TwitterStreamProcessor(tweepy.StreamListener):
    def processStatus(self,status):
        dic= {}
        dic['tweetID'] = status.id_str
        dic['userID'] = status.user.id_str
        dic['userName']= status.user.name
        dic['location']=status.user.location
        dic['timeZone']=status.user.time_zone
        dic['createTime']=status.created_at
        dic['lang']=status.lang
        dic['tweet_text']=status.text
        print(dic)

    def on_status(self, status):
        p = Process(target=self.processStatus, args=(status,))
        p.start()
        

 
startStreaming()
