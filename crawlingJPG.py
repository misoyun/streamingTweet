import tweepy
import json
import urllib
import pprint

CREDENTIALS_FILENAME = 'creds-twitter.json'
jf = open(CREDENTIALS_FILENAME)
creds = json.load(jf)
jf.close()

CONSUMER_KEY = creds['CONSUMER_KEY']
CONSUMER_SECRET = creds['CONSUMER_SECRET']
ACCESS_TOKEN = creds['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = creds['ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

def downloadImage(url, filename):
    urllib.request.urlretrieve(url, filename)

openfile = open("twitterMediafile.txt", "w")

for status in tweepy.Cursor(api.user_timeline, id ='WannaOne_twt', tweet_mode = 'extended').items(1500):
    if status.full_text.find("워너원데이") > -1 :
        strg = '{:%Y-%m-%d}'.format(status.created_at)
        openfile.write(strg)
        openfile.write('\n')
        print(strg)
        txt = status.full_text
        openfile.write(txt)
        openfile.write('\n')
        n = 1

        try :    
            for image in status.extended_entities['media'] :
                url = image['media_url']
                openfile.write(url)
                openfile.write('\n')
                filename = ('./WannaOneDay/' + strg + '-%d.jpg' % n)
                downloadImage(url, filename)
                n += 1
        except AttributeError as error :
            try :
                for image in status.entities['media'] :
                    url = image['media_url']
                    openfile.write(url)
                    openfile.write('\n')
                    filename = ('./WannaOneDay/' + strg + '-%d.jpg' % n)
                    downloadImage(url, filename)
                    n += 1
            except :
                print('error: '+strg)
                pass
                
openfile.close()
