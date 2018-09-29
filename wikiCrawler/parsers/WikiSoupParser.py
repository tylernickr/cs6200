from bs4 import BeautifulSoup
import re

class WikiSoupParser(object):

    def __init__(self):
        self.page = None

    def parse(self, html):
        self.page = BeautifulSoup(html, 'html.parser')

    def extractLinks(self):
        body = self.page.find('div', attrs={ 'class':'mw-parser-output' }) # Only concerned with links in the body
        links = []
        for child in body.findChildren():
            if child.find('div', attrs={ 'class': 'mw-references-wrap'}) != None:
                break

            child_links = child.findAll('a')
            for link in child_links:
                url = link.get('href')
                if url:
                    links.append(url)

        links = self._remove_same_page_segments(links)
        links = self._dedup_link_list(links)
        links = self._wiki_only(links)

        return links

    def _dedup_link_list(self, links):
        link_dict = {}
        for link in links:
            link_dict[link] = 1
        return list(link_dict.keys())

    def _wiki_only(self, links):
        links = [x for x in links if re.match('^/wiki/', x)]
        links = [x for x in links if not re.match('.*:.*', x)]
        return links

    def _remove_same_page_segments(self, links):
        results = []
        for link in links:
            try:
                results.append(link[:link.index('#')])
            except ValueError as e:
                results.append(link)

        return results

