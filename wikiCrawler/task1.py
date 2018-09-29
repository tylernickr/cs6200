from wikiCrawler.wikicrawler import WikiCrawler as wc
from wikiCrawler.parsers import WikiSoupParser as ps
from wikiCrawler.frontiermanagers import FrontierManager as fm

SEED_URL = '/wiki/Time_zone'
DELAY_SECONDS = 1

if __name__ == '__main__':
    crawler = wc.WikiCrawler(DELAY_SECONDS)
    crawler.set_parser(ps.WikiSoupParser())
    crawler.set_frontier_manager(fm.FrontierManager())
    crawler.crawl(SEED_URL, 6)
