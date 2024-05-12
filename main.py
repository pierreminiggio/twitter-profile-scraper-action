import sys

sys.path.insert(0, 'scraper/scraper')

from scraper.scraper.twitter_scraper import Twitter_Scraper

args = sys.argv

if len(args) != 4:
    print('Use like this : python main.py <mail> <username> <password>')
    sys.exit()

scraper = Twitter_Scraper(
    mail=args[1],
    username=args[2],
    password=args[3],
)

print(scraper)
