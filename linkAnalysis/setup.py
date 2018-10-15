from setuptools import setup
from os import makedirs

try:
    makedirs('./output_files/')
except:
    pass

try:
    makedirs('./input_files/Carbon_footprint')
except:
    pass

try:
    makedirs('./input_files/Focused_Crawl')
except:
    pass

setup(name='linkAnalysis',
      version='1.0',
      packages=['graphCreator',
                'pageRank',
                'parsers'])