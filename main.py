import tweepy
import time

# Initialization
auth = tweepy.OAuth1UserHandler(
   "PYmsYWW9uUptZUNNiG1kYgK9d", "73AQpBn1WmHFXtHyvtqeOTSOts7X68LfgYqcRSBcFx6pLgEvz4",
   "1580455034172719104-alsgtl5IQDKrvHwjOOthZasxEMOebw", "kb6mbOvdxjGwXuLKno3doXM7CgPtqD0cjiygfscn4BjQB"
)
api = tweepy.API(auth)

# Getting Bot ID
bot_id = int(api.me().id_str)

mention_id = 1
