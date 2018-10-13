class PageRank(object):

    def run_page_rank(self, node_graph):
        delta = 999
        self.current_page_rank = self._get_initial_page_rank(node_graph)

        while delta > .0001:
            n = len(list(node_graph.keys())) # N (Number of pages)
            new_page_rank = self._get_blank_pr_dict(node_graph)
            total_sink_pr = self._get_sink_pr(node_graph)
            for node in node_graph.keys():
                new_page_rank[node] = (1 - .85) / n
                new_page_rank[node] += .85 * total_sink_pr / n
                for inlink in node_graph[node]:
                    outlinks_in_inlink = self._get_outlinks(inlink, node_graph)
                    new_page_rank[node] += .85 * self.current_page_rank[inlink] / outlinks_in_inlink
            delta = self._get_delta_over_page_ranks(self.current_page_rank, new_page_rank)
            for node in self.current_page_rank.keys():
                self.current_page_rank[node] = new_page_rank[node]
        return sorted(self.current_page_rank.items(), key=lambda x: -x[1])

    def _get_delta_over_page_ranks(self, old_ranking, new_ranking):
        delta = 0
        for node in old_ranking.keys():
            delta += abs(old_ranking[node] - new_ranking[node])
        return delta

    def _get_outlinks(self, node, node_graph):
        outlinks = 0
        for inlink_list in node_graph.values():
            for inlink in inlink_list:
                if inlink == node:
                    outlinks += 1
        return outlinks

    def _get_sink_pr(self, node_graph):
        total_sink_pr = 0
        sink_node = self._get_sink_nodes(node_graph)
        for node in sink_node:
            total_sink_pr += self.current_page_rank[node]
        return total_sink_pr

    def _get_sink_nodes(self, node_graph):
        sink_nodes = []
        for node in node_graph.keys():
            sink_node = True
            for inlink_set in node_graph.values():
                for inlink in inlink_set:
                    if inlink == node:
                        sink_node = False
            if sink_node:
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

    rank = PageRank()
    print(rank.run_page_rank(testDict))
