import tweepy # for tweeting
from secrets import *# shhhh
from book_manager import BookManager # for getting sentences out of our book file
import datetime

def get_next_chunk():
  # open text file
  book = BookManager()
  first_sentence = book.first_sentence()
  # tweet the whole sentence if it's short enough
  if len(first_sentence) <= 140:
    chunk = first_sentence
  # otherwise just print the first 140 characters
  else:
    chunk = first_sentence[0:140]

  # delete what we just tweeted from the text file
  book.delete_message(chunk)
  return chunk

#NOTE: isItTuesday() will not post a tweet twice in a row on the same day.
#This is because Twitter does not allow the posting of tweets
# that are a duplicate to the most recent tweet
# isItTuesday utilizes datetime library
def isItTuesday():
    t =datetime.date.today().weekday
    if t == 1: #If it is Tuesday
	tweet("It is Tuesday!!")
    else: #If it is another day of the week
        tweet("It is not Tuesday =[ =[")

def tweetTo(message, account):
    secret = secrets[account]
    auth = tweepy.OAuthHandler(secret.consumer_key, secret.consumer_secret)
    auth.set_access_token(secret.access_token, secret.access_token_secret)
    api = tweepy.API(auth)
    auth.secure = True
    print("Posting message {}".format(message))
    api.update_status(status=message)    


def tweet(message):
    for secret in secrets:
      auth = tweepy.OAuthHandler(secret.consumer_key, secret.consumer_secret)
      auth.set_access_token(secret.access_token, secret.access_token_secret)
      api = tweepy.API(auth)
      auth.secure = True
      print("Posting message {}".format(message))
      api.update_status(status=message)


if __name__ == '__main__':
    #tweet(get_next_chunk())
    isItTuesday()
