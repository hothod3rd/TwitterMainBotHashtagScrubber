from twython import TwythonStreamer
import unicodedata
from TwitterProjectAuth import(
    costmerK,
    costmerSK,
    apiK,
    apiSK,
)
class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print (str(unicodedata.normalize('NFKD', (data['text'])).encode('ascii','ignore')))
            WriteFile = open('output.txt', 'a')
            WriteFile.write(str(unicodedata.normalize('NFKD', (data['text'])).encode('ascii','ignore')) + "\n")
            WriteFile.close()
channel = MyStreamer(
    costmerK,
    costmerSK,
    apiK,
    apiSK,
)
##Tells twython what to filter and how to i.e. use channel keys to check statuses and filter out anything that doesnt include #instagramdown
channel.statuses.filter(track='#MeanGirlsDay')


