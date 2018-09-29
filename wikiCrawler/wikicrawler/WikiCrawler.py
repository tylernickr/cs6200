from requests import *
from time import sleep


class WikiCrawler(object):
    ROOT_URL = "https://en.wikipedia.org/"

    def __init__(self, delay):
        self.delay = delay
        self.current_depth = 1

    def set_parser(self, parser):
        self.parser = parser

    def set_frontier_manager(self, frontier_manager):
        self.frontier_manager = frontier_manager

    def crawl(self, seed_url, max_depth):
        self.frontier_manager.add(seed_url, self.current_depth)
        while (self.frontier_manager.has_next()):
            sleep(self.delay) #IAmANiceCrawler
            url_to_crawl, url_depth = self.frontier_manager.next()
            url_to_crawl = WikiCrawler.ROOT_URL + url_to_crawl
            print(url_to_crawl + '\t\t' + str(url_depth))
            self.current_depth = url_depth
            response = get(url_to_crawl)
            self.process_response(response)

    def process_response(self, response):
        if response.status_code == 200:
            self.parser.parse(response.text)
            extracted_links = self.parser.extractLinks()
            for link in extracted_links:
                self.frontier_manager.add(link, self.current_depth + 1)
        else:
            print("Header: " + str(response.status_code))
            print("URL: " + response.url)