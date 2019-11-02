#Author: James Grace
#Date: 2nd November 2019
#Version: 0.2

import twython
from actions import *

############### APPLICATION DETAILS ###############
twitterHandle=""
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

###################################################
print("Twitter Control - Created by James Grace")
print("GitHub https://github.com/JamesPython1/twittercontrol/\n")

class TwitterControl(twython.TwythonStreamer):
    def on_success(self, data):
        print("Received tweet from @{0}: {1}".format(data['user']['screen_name'],data['text']))
        print("\n")
        actionsToDo=[]
        for word in keywords:
            if word in data['text']:
                actionsToDo.append(word)
        print(actionsToDo)
        for item in actionsToDo:
            index=keywords.index(item)
            try:
                p=actions[index]()
            except:
                print("Error running function for keyword: "+item)

stream = TwitterControl(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
while True:
    stream.statuses.filter(track=twitterHandle)

