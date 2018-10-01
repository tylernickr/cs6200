WikiCrawler
-

**This guide assumes we are using python 3.**

Prerequisites:

- This project uses BeautifulSoup! This will need to be installed on the 
machine before this is run/setup. The setup files will not do this installation 
on behalf of whoever is running it. This is the only third-party
library being used.
- This project also makes use of the linux dictionary located in: /usr/share/dict/words
- A copy of this wordlist is bundled with the distro


Steps to run this project:
- Unzip the distributed zip package and cd into the directory.
- You should see a few setup.py files and two folders (wikiCrawler, resource)
run "python setup[12|3].py install" depending on which task you want to run.
- You should also see a hw_results director which has the .txt files for the HW in it. These are the link lists with no more than 1000 links, etc.
- Tasks 1 and 2 are combined into setup12.py and task12.py
- You should see an output_files folder get created
- Next, run "python wikiCrawler/task12.py" to run tasks 1 and 2
- Run "python wikiCrawler/task3.py [url] [keywords...]"
- The url should be the form "/wiki/[seed_page]", The parser knows the wikipedia root, are we are limiting this to wikipedia after all
- The run for the task in the HW was "python wikiCrawler/task3.py "/wiki/Carbon_footprint" green"

References used:

- BeautifulSoup was used to suppliment the parser object in the codebase