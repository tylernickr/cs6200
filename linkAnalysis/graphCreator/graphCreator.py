from os import path, listdir
from pathlib import Path
from re import match
from lib.parsers import WikiSoupParser as parse

class GraphCreator(object):

    def __init__(self, root_dir):
        dirs = [x for x in listdir(root_dir) if path.isdir(path.join(root_dir, x))]
        self.root_dir = root_dir
        self.dirs = dirs

    def create_graph(self):
        parser = parse.WikiSoupParser()
        graph = {}

        x = 1
        for dir in self.dirs:
            print(x)
            file = path.join(self.root_dir, dir, dir + '.html')
            file_contents = Path(file).read_text()
            parser.parse(file_contents)
            links = parser.extractLinks()
            for link in links:
                node = match('/wiki/(.*)$', link[0]).group(1)
                try:
                    graph[node].append(dir)
                except KeyError:
                    graph[node] = [dir]
            print(len(graph))
            x += 1

if __name__ == '__main__':
    gc = GraphCreator('/home/nick/Documents/InformationRetr/HW2/CrawledDocs/Carbon_footprint')
    gc.create_graph()
