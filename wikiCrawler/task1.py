from wikiCrawler.wikicrawler import WikiCrawler as wc
from wikiCrawler.parsers import WikiSoupParser as ps

SEED_URL = 'Time_zone'
DELAY_SECONDS = 1

if __name__ == '__main__':
    crawler = wc.WikiCrawler(DELAY_SECONDS)
    crawler.set_parser(ps.WikiSoupParser())
    crawler.crawl(SEED_URL, 6)
