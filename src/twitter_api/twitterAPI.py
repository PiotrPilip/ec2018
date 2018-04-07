import tweepy
import sys
import time
import datetime
sys.path.append('../master_database_pusher/')
from multiprocessing import Process, Queue
from configparser import ConfigParser as ConfPar
from trackNames import trackNames
import mdp_database_queries as mdq
globalQueue = Queue()

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

def getStreamListener(twitterApi,tracknames=trackNames):
    streamListener = TwitterStreamProcessor(tracknames)
    twitterStream = tweepy.Stream(auth = twitterApi.auth, listener=streamListener)
    return twitterStream

def startStreaming():
    api=getTwitterApi()
    twitterStream=getStreamListener(api)
    twitterStream.filter(track=trackNames)
    
    
class TwitterStreamProcessor(tweepy.StreamListener):
    twitterTrackNames=0
    def __init__(self,trackNames):
        self.twitterTrackNames=trackNames
        tweepy.StreamListener.__init__(self)
        
    def processStatus(self,status,twitterTrackNames,dataStore):
        def findTrackname(twitterTrackNames, text):
            foundNames = []
            tmpText = text
            tmpText = tmpText.lower()
            for trackName in twitterTrackNames:
                if trackName in tmpText:
                    foundNames.append(trackName)
            return foundNames

        dic= {}
        dic['tweetID'] = int(status.id_str)
        dic['userID'] = int(status.user.id_str)
        dic['userName']= status.user.name
        dic['location']= status.user.location
        dic['time_zone']= status.user.time_zone
        dic['createtime']= int(status.created_at.strftime('%s'))
        dic['lang']=status.lang
        dic['tweet_text']=status.text
        tmp = findTrackname(twitterTrackNames,status.text)
        if not tmp==[]:
            print(tmp[0])
            dataStore.put(dic)
            mdq.insert_twitter_dic(dic,tmp[0])
        
        
    def on_status(self, status):
        p = Process(target=self.processStatus, args=(status,self.twitterTrackNames,globalQueue,))
        p.start()
        
###################
def getTweetLang(langDic,tweet):
    if tweet['lang'] in langDic:
        langDic[tweet['lang']]=langDic[tweet['lang']]+1
    else:
        langDic[tweet['lang']]=1


def RealTimeCollector(queue,collectingTime=10):
    open('counterData.txt', 'w').close()
    open('langData.txt','w').close()
    while True:
        start = time.time()
        time.clock()
        elapsed = 0
        counter=0
        langDic={}
        while elapsed < collectingTime:
            elapsed = time.time() - start
            if not queue.empty():
                tweet=queue.get()
                getTweetLang(langDic,tweet)
                counter=counter+1
                
        print("SAVING...")
        with open("counterData.txt", "a") as myfile:
            myfile.write(str(datetime.datetime.now())+'='+str(counter)+"\n")
        with open("langData.txt", "a") as myfile:
            myfile.write(str(datetime.datetime.now())+'='+str(langDic)+"\n")


        
p1=Process(target=RealTimeCollector,args=(globalQueue,))
p1.start()
startStreaming()
