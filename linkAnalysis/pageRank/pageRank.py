class PageRank(object):

    def __init__(self, dampen_factor):
        self.dampen_factor = dampen_factor

    def get_norms(self):
        return self.norms

    def run_page_rank(self, inlink_graph, outlink_graph, number_of_iterations):
        if number_of_iterations == None:
            number_of_iterations = 99999
        delta = 999
        iterations = 1
        self.current_page_rank = self._get_initial_page_rank(inlink_graph)
        self.outlink_graph = outlink_graph
        self.norms = []

        while delta > .0001 and iterations <= number_of_iterations:
            n = len(list(inlink_graph.keys())) # N (Number of pages)
            new_page_rank = self._get_blank_pr_dict(inlink_graph)
            total_sink_pr = self._get_sink_pr(inlink_graph)
            for node in inlink_graph.keys():
                new_page_rank[node] = (1 - self.dampen_factor) / n
                new_page_rank[node] += self.dampen_factor * total_sink_pr / n
                for inlink in inlink_graph[node]:
                    outlinks_in_inlink = self._get_outlinks(inlink)
                    new_page_rank[node] += self.dampen_factor * self.current_page_rank[inlink] / outlinks_in_inlink
            delta = self._get_delta_over_page_ranks(self.current_page_rank, new_page_rank)
            self.norms.append((delta, sum(new_page_rank.values())))
            for node in self.current_page_rank.keys():
                self.current_page_rank[node] = new_page_rank[node]
            iterations += 1
        return sorted(self.current_page_rank.items(), key=lambda x: -x[1])

    def _get_delta_over_page_ranks(self, old_ranking, new_ranking):
        delta = 0
        for node in old_ranking.keys():
            delta += abs(old_ranking[node] - new_ranking[node])
        return delta

    def _get_outlinks(self, node):
        return len(self.outlink_graph[node])

    def _get_sink_pr(self, node_graph):
        total_sink_pr = 0
        sink_node = self._get_sink_nodes()
        for node in sink_node:
            total_sink_pr += self.current_page_rank[node]
        return total_sink_pr

    def _get_sink_nodes(self):
        sink_nodes = []
        for node, outlinks in self.outlink_graph.items():
            if len(outlinks) == 0:
                sink_nodes.append(node)
        return sink_nodes

    def _get_initial_page_rank(self, node_graph):
        init_page_rank = {}
        n = len(node_graph.keys())
        for node in node_graph.keys():
            init_page_rank[node] = 1 / n
        return init_page_rank

    def _get_blank_pr_dict(self, node_graph):
        blank_dict = {}
        for node in node_graph.keys():
            blank_dict[node] = None
        return blank_dict


if __name__ == '__main__':
    testDict = {}
    testDict['A'] = ['D', 'E', 'F']
    testDict['B'] = ['A', 'F']
    testDict['C'] = ['A', 'B', 'D']
    testDict['D'] = ['B', 'C']
    testDict['E'] = ['B', 'C', 'D', 'F']
    testDict['F'] = ['A', 'B', 'D']

    testOut = {}
    testOut['A'] = ['B', 'C', 'F']
    testOut['B'] = ['D', 'E', 'F']
    testOut['C'] = ['D', 'E']
    testOut['D'] = ['A', 'C', 'E', 'F']
    testOut['E'] = ['A']
    testOut['F'] = ['A', 'B', 'E']

    rank = PageRank()
    print(rank.run_page_rank(testDict, testOut))
