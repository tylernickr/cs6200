from wikiCrawler.wikicrawler import WikiCrawler as wc, LinkJournal as lj
from wikiCrawler.parsers import WikiSoupParser as ps
from wikiCrawler.frontiermanagers import FrontierManager as fm
from wikiCrawler.storagemanagers import StorageManager as sm
from wikiCrawler.relevengines import RelevanceEngine as rev

DELAY_SECONDS = 1
DICT_LOC = './resource/words.txt'
OUTPUT_DIR = './output_files/'

if __name__ == '__main__':
    crawler = wc.WikiCrawler(DELAY_SECONDS)
    crawler.set_parser(ps.WikiSoupParser())
    crawler.set_frontier_manager(fm.FrontierManager())
    crawler.set_storage_manager(sm.StorageManager(OUTPUT_DIR))
    crawler.set_relevance_engine(rev.RelevanceEngine(DICT_LOC, []))
    crawler.crawl('/wiki/Time_zone', 6, 10)

    crawler2 = wc.WikiCrawler(DELAY_SECONDS)
    crawler2.set_parser(ps.WikiSoupParser())
    crawler2.set_frontier_manager(fm.FrontierManager())
    crawler2.set_storage_manager(sm.StorageManager(OUTPUT_DIR))
    crawler2.set_relevance_engine(rev.RelevanceEngine(DICT_LOC, []))
    crawler2.crawl('/wiki/Electric_car', 6, 10)

    crawler3 = wc.WikiCrawler(DELAY_SECONDS)
    crawler3.set_parser(ps.WikiSoupParser())
    crawler3.set_frontier_manager(fm.FrontierManager())
    crawler3.set_storage_manager(sm.StorageManager(OUTPUT_DIR))
    crawler3.set_relevance_engine(rev.RelevanceEngine(DICT_LOC, []))
    crawler3.crawl('/wiki/Carbon_footprint', 6, 10)

    myjournal = lj.LinkJournal()

    try:
        file1 = open('./output_files/time_zone_links.txt', 'w')
        file2 = open('./output_files/electric_car_links.txt', 'w')
        file3 = open('./output_files/carbon_footprint_links.txt', 'w')
        file4 = open('./output_files/merged_links.txt', 'w')

        file1.write("URL\tDepth\tTitleCloseness\n")
        file2.write("URL\tDepth\tTitleCloseness\n")
        file3.write("URL\tDepth\tTitleCloseness\n")
        file4.write("URL\tDepth\tTitleCloseness\n")
        for item in crawler.get_crawled_list():
            file1.write(item[0] + '\t\t' + str(item[1]) + '\t\t' + str(item[2]) + '\n')
            myjournal.add(item[0], item[1], item[2])
        file1.close()
        for item in crawler2.get_crawled_list():
            file2.write(item[0] + '\t\t' + str(item[1]) + '\t\t' + str(item[2]) + '\n')
            myjournal.add(item[0], item[1], item[2])
        file2.close()
        for item in crawler3.get_crawled_list():
            file3.write(item[0] + '\t\t' + str(item[1]) + '\t\t' + str(item[2]) + '\n')
            myjournal.add(item[0], item[1], item[2])
        file3.close()
        for item in myjournal.get_ordered_journal():
            file4.write(item[0] + '\t\t' + str(item[1]) + '\t\t' + str(item[2]) + '\n')
            myjournal.add(item[0], item[1], item[2])
        file4.close()

    except IOError:
        print("Something went horribly wrong")
        exit(1)