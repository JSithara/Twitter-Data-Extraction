from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
 
import authentication
 
class MyStreamListener(StreamListener):
    def __init__(self):
        super().__init__()
        self.start=0
        self.stop=2000
    def on_data(self, data):
        filePath = 'twitDB.json'
        perm = 'a'
        print(self.start)
        if(self.start == self.stop):
            saveFile = open(filePath,perm)
            saveFile.write(data)
            saveFile.write("]")      
            saveFile.close()
            return False
        if(self.start == 0):
            saveFile = open(filePath,perm)
            saveFile.write("[")     
            saveFile.write(data)
            saveFile.write(",")  
            saveFile.close()
        else:
            saveFile = open(filePath,perm)     
            saveFile.write(data) 
            saveFile.write(",")
            saveFile.close()
        self.start = self.start + 1
        return True

    
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False

 
if __name__ == '__main__':
 
    # Authenticate using config.py and connect to Twitter Streaming API.
    listener = MyStreamListener()
    auth = OAuthHandler(authentication.CONSUMER_KEY, authentication.CONSUMER_SECRET)
    auth.set_access_token(authentication.ACCESS_TOKEN, authentication.ACCESS_TOKEN_SECRET)
    stream = Stream(auth, listener)
    stream.filter(track=['Canada','Canada import','Canada export','Canada Education','Canada vehicle sales'])