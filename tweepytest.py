import tweepy

consumer_key="tjnuF5hLptGQD6inWw2ArYBpl"
consumer_secret="oDqvsMRoYJXknX8Ldb80y2DDrlDwEyvkDObDXdU21gQqTqA5DI"
access_token="981945472070963200-9QaeApfU2tXi8Rt7WubEYpbvnHcRIZI"
access_token_secret="csU1xsHmAnnrFDx5cwActRISn90OGQcbfS8EyFA6ubhbJ"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)
        