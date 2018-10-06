from twython import TwythonStreamer
from twython import Twython
import unicodedata
from TpAUTH import(
    costmerK,
    costmerSK,
    apiK,
    apiSK,
)
class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        global twitter
        splitPt1 = ["",""]
        splitPt2 = ["",""]
        imgUrl = ["","","",""]
        proPic = ""
        usrName = ""
        contentBody = ""
        if 'text' in data:
            splitPt1 = ((str(unicodedata.normalize('NFKD', (data['text'])).encode('ascii','ignore'))).split(":", 1))
            if ("@" in splitPt1[0]):
                splitPt2 = ((splitPt1[0]).split("@", 1))
                print (str(unicodedata.normalize('NFKD', (data['text'])).encode('ascii','ignore')))
                if splitPt2[1] == "":
                    details = twitter.show_user(screen_name=str(splitPt2[1]))
                    if "https" in splitPt1[1]:
                        imgUrl[0] = splitPt1[1].split("https", 1)
                    else:
                        imgUrl[0] = splitPt1[1]
                    print (details['profile_image_url'])
                    usrName = str(splitPt2[1])
                    contentBody = str(imgUrl[0])
                    proPic = (details['profile_image_url'])
                    WriteFile = open('output.txt', 'a')
                    endWrite = (proPic + "£££" + usrName + "£££" + contentBody)
                    endWrite = (endWrite.replace("\n", " "))
                    WriteFile.write(endWrite)
                    WriteFile.write("\n")
                    WriteFile.close()
channel = MyStreamer(
    costmerK,
    costmerSK,
    apiK,
    apiSK,
)
twitter = Twython(
    costmerK,
    costmerSK,
    apiK,
    apiSK,
)
##Tells twython what to filter and how to i.e. use channel keys to check statuses and filter out anything that doesnt include #instagramdown
channel.statuses.filter(track='#FridayFeeling', tweet_mode='extended')


