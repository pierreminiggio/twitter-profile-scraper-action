import json
import os
import sys

sys.path.insert(0, 'scraper/scraper')

from scraper.scraper.twitter_scraper import Twitter_Scraper

args = sys.argv

if len(args) != 5 and len(args) != 6:
    print('Use like this : python main.py <username_to_scrape> <mail> <username> <password> [proxy]')
    sys.exit()

username = args[3]
proxy = args[5] if len(args) == 6 else None

scraper = Twitter_Scraper(
    mail=args[2],
    username=username,
    password=args[4],
    proxy=proxy
)

scraper.login()

scraper.scrape_tweets(
    scrape_query='(from:' + args[1] + ')'
)

tweets = scraper.get_tweets()

tweets_file_path = 'tweets.json'

if os.path.exists(tweets_file_path):
    os.remove(tweets_file_path)

tweets_file = open(tweets_file_path, 'a')
tweets_file.write(json.dumps(tweets))
tweets_file.close()

if not scraper.interrupted:
    scraper.driver.close()
