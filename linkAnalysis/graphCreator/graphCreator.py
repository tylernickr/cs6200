from os import path, listdir
from pathlib import Path
from re import match
from parsers import WikiSoupParser as parse


class GraphCreator(object):

    def __init__(self, root_dir):
        dirs = [x for x in listdir(root_dir) if path.isdir(path.join(root_dir, x))]
        self.root_dir = root_dir
        self.dirs = dirs

    def create_graph(self):
        parser = parse.WikiSoupParser()
        inlink_graph = {}
        outlink_graph = {}

        x = 1
        for dir in self.dirs:
            if x % 100 == 0:
                print(x)
            file = path.join(self.root_dir, dir, dir + '.html')
            file_contents = Path(file).read_text()
            parser.parse(file_contents)
            links = parser.extractLinks()
            outlink_graph[dir] = []
            for link in links:
                node = match('/wiki/(.*)$', link[0]).group(1)
                outlink_graph[dir].append(node)
                try:
                    if dir not in inlink_graph[node]:
                        inlink_graph[node].append(dir)
                except KeyError:
                    inlink_graph[node] = [dir]
            x += 1

        to_pop = self._get_nodes_to_pop(inlink_graph)
        for node in to_pop:
            inlink_graph.pop(node)

        for node in inlink_graph.keys():
            filtered_list = []
            for inlink in inlink_graph[node]:
                if inlink in self.dirs:
                    filtered_list.append(inlink)
            inlink_graph[node] = filtered_list

        for node in outlink_graph.keys():
            filtered_list = []
            for outlink in outlink_graph[node]:
                if outlink in self.dirs:
                    filtered_list.append(outlink)
            outlink_graph[node] = filtered_list

        # Add in nodes with no inlinks
        for dir in self.dirs:
            if dir not in inlink_graph.keys():
                inlink_graph[dir] = []

        # Add in nodes with no outlinks
        for dir in self.dirs:
            if dir not in outlink_graph.keys():
                outlink_graph[dir] = []

        return (inlink_graph, outlink_graph)

    def _get_nodes_to_pop(self, graph):
        to_pop = []
        for node in graph.keys():
            if node not in self.dirs:
                to_pop.append(node)

        return to_pop


if __name__ == '__main__':
    gc = GraphCreator('')
    gc.create_graph()
