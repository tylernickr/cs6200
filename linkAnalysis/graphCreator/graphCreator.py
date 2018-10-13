from os import path, listdir

class GraphCreator(object):

    def __init__(self, root_dir):
        dirs = [x for x in listdir(root_dir) if path.isdir(path.join(root_dir, x))]
        self.dirs = dirs
        print(dirs)


if __name__ == '__main__':
    GraphCreator('/home/nick/Documents/InformationRetr/HW2/CrawledDocs/Carbon_footprint')
