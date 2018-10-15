from graphCreator.graphCreator import GraphCreator
from pageRank.pageRank import PageRank
from os import makedirs, path
from argparse import ArgumentParser

#Modify these as needed for your root directories
ROOT_DIR_CFOOTPRINT = './input_files/Carbon_footprint'
ROOT_DIR_FOCUSED_CRAWL = './input_files/Focused_Crawl'

OUTPUT_DIR = './output_files/'
G1_GRAPH_FILE = OUTPUT_DIR + 'g1_graph.txt'
G1_NORM_FILE = OUTPUT_DIR + 'g1_norms.txt'
G1_PAGE_RANK_RESULTS = OUTPUT_DIR + 'g1_page_rank_results.txt'
G1_STATS_FILE = OUTPUT_DIR + 'g1_graph_statistics.txt'
G1_INLINK_SORT = OUTPUT_DIR + 'g1_inlink_sort.txt'

G2_GRAPH_FILE = OUTPUT_DIR + 'g2.graph.txt'
G2_NORM_FILE = OUTPUT_DIR + 'g2_norms.txt'
G2_PAGE_RANK_RESULTS = OUTPUT_DIR + 'g2_page_rank_results.txt'
G2_STATS_FILE = OUTPUT_DIR + 'g2_graph_statistics.txt'
G2_INLINK_SORT = OUTPUT_DIR + 'g2_inlink_sort.txt'


if __name__ == '__main__':
    parser = ArgumentParser(description='Create a graph and then apply page rank')
    parser.add_argument('dampen_factor', type=float, help='factor to use in dampening')
    parser.add_argument('--pr_iterations', required=False, type=int, help='Number of iterations of pagerank to run. Default is until convergance.', )
    args = parser.parse_args()

    # Run One
    stats = {}
    pr = PageRank(args.dampen_factor)
    gc = GraphCreator(ROOT_DIR_CFOOTPRINT)
    inlink_graph, outlink_graph = gc.create_graph()
    no_in_links = [node for node in inlink_graph.keys() if len(inlink_graph[node]) == 0]
    no_out_links = [node for node in outlink_graph.keys() if len(outlink_graph[node]) == 0]
    max_in_degree = sorted([len(x) for x in inlink_graph.values()], key=lambda x: -x)[0]
    max_out_degree = sorted([len(x) for x in outlink_graph.values()], key=lambda x: -x)[0]
    rankings = pr.run_page_rank(inlink_graph, outlink_graph, args.pr_iterations)
    l1_norms = pr.get_norms()
    if not path.exists(OUTPUT_DIR):
        makedirs(OUTPUT_DIR)

    with open(G1_INLINK_SORT, 'w') as inlink_sort_file:
        sorted_inlinks = sorted(inlink_graph.items(), key=lambda x: -len(x[1]))
        for link in sorted_inlinks[:20]:
            print(link[0] + ': ' + str(len(link[1])) + ' inlinks', file=inlink_sort_file)

    with open(G1_STATS_FILE, 'w') as stats_file:
        print('No in-link pages (' + str(len(no_in_links)) + '): ' + str(no_in_links), file=stats_file)
        print('No out-link pages (' + str(len(no_out_links)) + '): ' + str(no_out_links), file=stats_file)
        print('Max in-degree: ' + str(max_in_degree), file=stats_file)
        print('Max out-degree: ' + str(max_out_degree), file=stats_file)

    with open(G1_GRAPH_FILE, 'w') as graph_file:
        for page, inlinks in inlink_graph.items():
            print(page + ': ' + str(inlinks), file=graph_file)

    with open(G1_NORM_FILE, 'w') as norm_file:
        for norm in l1_norms:
            print(str(norm[0]) + ', ' + str(norm[1]), file=norm_file)

    with open(G1_PAGE_RANK_RESULTS, 'w') as page_rank_file:
        for page, rank in rankings[:50]:
            print(page + ':\t' + str(rank), file=page_rank_file)

    #Run Two
    pr = PageRank(args.dampen_factor)
    gc = GraphCreator(ROOT_DIR_FOCUSED_CRAWL)
    inlink_graph, outlink_graph = gc.create_graph()
    no_in_links = [node for node in inlink_graph.keys() if len(inlink_graph[node]) == 0]
    no_out_links = [node for node in outlink_graph.keys() if len(outlink_graph[node]) == 0]
    max_in_degree = sorted([len(x) for x in inlink_graph.values()], key=lambda x: -x)[0]
    max_out_degree = sorted([len(x) for x in outlink_graph.values()], key=lambda x: -x)[0]
    rankings = pr.run_page_rank(inlink_graph, outlink_graph, args.pr_iterations)
    l1_norms = pr.get_norms()
    if not path.exists(OUTPUT_DIR):
        makedirs(OUTPUT_DIR)

    with open(G2_INLINK_SORT, 'w') as inlink_sort_file:
        sorted_inlinks = sorted(inlink_graph.items(), key=lambda x: -len(x[1]))
        for link in sorted_inlinks[:20]:
            print(link[0] + ': ' + str(len(link[1])) + ' inlinks', file=inlink_sort_file)

    with open(G2_STATS_FILE, 'w') as stats_file:
        print('No in-link pages (' + str(len(no_in_links)) + '): ' + str(no_in_links), file=stats_file)
        print('No out-link pages (' + str(len(no_out_links)) + '): ' + str(no_out_links), file=stats_file)
        print('Max in-degree: ' + str(max_in_degree), file=stats_file)
        print('Max out-degree: ' + str(max_out_degree), file=stats_file)

    with open(G2_GRAPH_FILE, 'w') as graph_file:
        for page, inlinks in inlink_graph.items():
            print(page + ': ' + str(inlinks), file=graph_file)

    with open(G2_NORM_FILE, 'w') as norm_file:
        for norm in l1_norms:
            print(str(norm[0]) + ', ' + str(norm[1]), file=norm_file)

    with open(G2_PAGE_RANK_RESULTS, 'w') as page_rank_file:
        for page, rank in rankings[:50]:
            print(page + ':\t' + str(rank), file=page_rank_file)