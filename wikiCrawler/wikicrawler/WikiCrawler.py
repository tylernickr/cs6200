from requests import *
from time import time
from wikiCrawler.wikicrawler.LinkJournal import LinkJournal


class WikiCrawler(object):
    ROOT_URL = "https://en.wikipedia.org/"

    def __init__(self, delay):
        self.delay = delay
        self.current_depth = 1
        self.last_crawl = 0
        self.pages_crawled = 0
        self.link_journal = LinkJournal()

    # For managing parsing
    def set_parser(self, parser):
        self.parser = parser

    # For managing the frontier
    def set_frontier_manager(self, frontier_manager):
        self.frontier_manager = frontier_manager

    # For managing storing the files (Turned off right now)
    def set_storage_manager(self, storage_manager):
        self.storage_manager = storage_manager

    # Set logic class for determining if something is relevant
    def set_relevance_engine(self, relevence_engine):
        self.relevence_engine = relevence_engine

    def crawl(self, seed_url, max_depth, max_pages):
        self.frontier_manager.add(seed_url, self.current_depth, 0)

        #Crawl intil we reach one of our limiting constraints or we run out of links
        while (self.frontier_manager.has_next() and self.link_journal.size() < max_pages):
            if time() - self.last_crawl < self.delay:
                continue
            self.last_crawl = time()
            url_to_crawl, url_depth, dist_ft = self.frontier_manager.next()
            url_to_crawl = WikiCrawler.ROOT_URL + url_to_crawl
            self.current_depth = url_depth

            # Handle the depth constraint
            if self.current_depth > max_depth:
                return
            self.link_journal.add(url_to_crawl, url_depth, dist_ft)
            response = get(url_to_crawl)
            self.process_response(url_to_crawl, response)
            self.pages_crawled += 1

    def process_response(self, url, response):
        if response.status_code == 200:
            self.storage_manager.store(url, response.text)
            self.parser.parse(response.text)
            extracted_links = self.parser.extractLinks()
            for link, link_text, dist_ft in extracted_links:
                if self.relevence_engine.is_url_relevant(link) or self.relevence_engine.is_text_relevant(link_text):  # Check for relevence
                    self.frontier_manager.add(link, self.current_depth + 1, dist_ft)

        else:
            # Was going to implement something here but I found I wasn't encountering them because of the
            # way I was extracting URLs.
            print("Header: " + str(response.status_code))
            print("URL: " + response.url)

    def get_crawled_list(self):
        return self.link_journal.get_ordered_journal()