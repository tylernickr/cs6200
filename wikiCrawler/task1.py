from wikiCrawler.wikicrawler import WikiCrawler as wc

SEED_URL = 'https://en.wikipedia.org/wiki/Time_zone'
DELAY_SECONDS = 2

if __name__ == '__main__':
    crawler = wc.WikiCrawler(DELAY_SECONDS)
    crawler.crawl(SEED_URL, 6)
