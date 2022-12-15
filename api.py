import tweepy
import time

# API情報を記入
BEARER_TOKEN        = ""
API_KEY             = ""
API_SECRET          = ""
ACCESS_TOKEN        = ""
ACCESS_TOKEN_SECRET = ""

# クライアント関数を作成
def ClientInfo():
    client = tweepy.Client(bearer_token    = BEARER_TOKEN,
                           consumer_key    = API_KEY,
                           consumer_secret = API_SECRET,
                           access_token    = ACCESS_TOKEN,
                           access_token_secret = ACCESS_TOKEN_SECRET,
                          )
    
    return client

# 取得したいキーワード  
search_list = ['']
search_num = 8

for search in search_list:
    # サーチ結果
    tweets = ClientInfo().search_recent_tweets(query = search, max_results = search_num)

    for i in range(search_num):
        tweet_id = tweets.data[i].id
        try:
            ClientInfo().like(tweet_id)
            print('いいね!!をしました')
            time.sleep(30)
        except tweepy.errors.TweepError as e:
            print(e.reason)
        except StopIteration:
            break