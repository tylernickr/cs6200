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
            # This is the content section of the page, get all the blocks
            if child.find('div', attrs={ 'class': 'mw-references-wrap'}) != None:
                break

            child_links = child.findAll('a')
            for link in child_links:
                dist_from_title = 0
                url = link.get('href')
                url_text = link.string
                if url_text == None:
                    url_text = ''
                for parent in link.parents:  # Now check how far from title we are
                    dist_from_title += 1
                    try:
                        if parent['id'] == 'bodyContent':  # Same level as title
                            break
                    except KeyError:
                        pass

                    if parent.name == 'table':
                        url = None
                if url:
                    links.append((url, url_text, dist_from_title))

        links = self._remove_same_page_segments(links)
        links = self._dedup_link_list(links)
        links = self._wiki_only(links)

        return links

    def _dedup_link_list(self, links):
        link_dict = {}
        results = []
        for link, link_text, dist_from_title in links:
            try:
                dist_from_title = max(dist_from_title, link_dict[link][1])
            except KeyError:
                pass

            link_dict[link] = (link_text, dist_from_title)
        for link, value in link_dict.items():
            results.append((link, value[0], value[1]))

        return results

    def _wiki_only(self, links):
        links = [x for x in links if re.match('^/wiki/', x[0])]
        links = [x for x in links if not re.match('.*:.*', x[0])]
        return links

    def _remove_same_page_segments(self, links):
        results = []
        for link, link_text, dist_from_title in links:
            try:
                results.append(((link[:link.index('#')]), link_text, dist_from_title))
            except ValueError as e:
                results.append((link, link_text, dist_from_title))

        return results

