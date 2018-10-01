from setuptools import setup
from os import makedirs

try:
    makedirs('./output_files/')
except:
    pass

setup(name='task3',
      version='1.0',
      packages=['wikiCrawler',
                'wikiCrawler.wikicrawler',
                'wikiCrawler.parsers',
                'wikiCrawler.frontiermanagers',
                'wikiCrawler.storagemanagers',
                'wikiCrawler.relevengines'])