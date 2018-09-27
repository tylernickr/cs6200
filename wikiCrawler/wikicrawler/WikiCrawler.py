from requests import *
from time import sleep


class WikiCrawler(object):
    ROOT_URL = "https://en.wikipedia.org/wiki/"

    def __init__(self, delay):
        self.delay = delay
        self.current_depth = 1
        self.todo_list = []
        self.done_list = []

    def set_parser(self, parser):
        self.parser = parser

    def crawl(self, seed_url, max_depth):
        seed_url = WikiCrawler.ROOT_URL + seed_url
        self.todo_list = [(seed_url, self.current_depth)]
        while (len(self.todo_list) > 0) and (self.todo_list[0][1] <= max_depth):
            sleep(self.delay) #IAmANiceCrawler
            url_to_crawl = self.todo_list[0][0]
            response = get(url_to_crawl)
            self.process_response(response)
            self.done_list += url_to_crawl
            self.todo_list = self.todo_list[1:]

    def process_response(self, response):
        if response.status_code == 200:
            self.parser.parse(response.text)
            print(self.parser.extractLinks())
        else:
            print("Header: " + str(response.status_code))
            print("URL: " + response.url)