from wikiCrawler.wikicrawler import WikiCrawler as wc
from wikiCrawler.parsers import WikiSoupParser as ps
from wikiCrawler.frontiermanagers import FrontierManager as fm
from wikiCrawler.storagemanagers import StorageManager as sm
from wikiCrawler.relevengines import RelevanceEngine as rev
from argparse import ArgumentParser

DELAY_SECONDS = 1
OUTPUT_DIR = './output_files/'
DICT_LOC = './resource/words.txt'

if __name__ == '__main__':
    parser = ArgumentParser(description='Run a focused crawl.')
    parser.add_argument('url', type=str, help='URL to start the crawl with.')
    parser.add_argument('keywords', type=str, nargs='+', help='The keywords to search for. Or logic is used')
    args = parser.parse_args()

    crawler = wc.WikiCrawler(DELAY_SECONDS)
    crawler.set_parser(ps.WikiSoupParser())
    crawler.set_frontier_manager(fm.FrontierManager())
    crawler.set_storage_manager(sm.StorageManager(OUTPUT_DIR))
    crawler.set_relevance_engine(rev.RelevanceEngine(DICT_LOC, args.keywords))
    crawler.crawl(args.url, 6, 1000)

    try:
        file1 = open('./output_files/focused_links.txt', 'w')

        file1.write("URL\tDepth\tTitleCloseness\n")
        for item in crawler.get_crawled_list():
            file1.write(item[0] + '\t\t' + str(item[1]) + '\t\t' + str(item[2]) + '\n')
        file1.close()

    except IOError:
        print("Something went horribly wrong")
        exit(1)