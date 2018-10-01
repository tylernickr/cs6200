WikiCrawler

This guide assumes we are using python 3.

Steps to run this project:
- Unzip the distributed zip package and cd into the directory.
- You should see a few setup.py files and two folders (wikiCrawler, resource)
run "python setup[12|3].py install" depending on which task you want to run.
- Tasks 1 and 2 are combined into setup12.py and task12.py
- You should see an output_files folder get created
- Next, run "python wikiCrawler/task12.py" to run tasks 1 and 2
- Run "python wikiCrawler/task3.py [url] [keywords...]"
- The url should be the form "/wiki/[seed_page]", The parser knows the wikipedia root, are we are limiting this to wikipedia after all
- The run for the task in the HW was "python wikiCrawler/task3.py "/wiki/Carbon_footprint" green"