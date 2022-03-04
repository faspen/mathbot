import tweepy
import time
verify_api = __import__('authorization').verify_api

api = verify_api()
myself = api.me()
FILE = "id.txt"

def retrive_id(file):
    """Retrive id from the id file"""
    f_read = open(file)
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_id(id, file):
    """Store given id to text file"""
    f_write = open(file, 'w')
    f_write.write(str(id))
    f_write.close()
    return

def fetch_equation(tweet):
    for i in range(len(tweet)):
        if tweet[i] == " ":
            equation = tweet[i:]
            break
    return equation

last_seen_id = retrive_id(FILE)
mentions = api.mentions_timeline(last_seen_id, tweet_mode="extended")


for mention in reversed(mentions):
    last_seen_id = mention.id
    store_id(last_seen_id, FILE)
    equation = fetch_equation(mention.full_text)
    try:
        solution = eval(equation)
        api.update_status("The answer is {}".format(solution), mention.id)
    except NameError:
        api.update_status("Do not pass in letters or words, please!", mention.id)