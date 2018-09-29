from re import match
from os import makedirs, path, remove

class StorageManager(object):

    def __init__(self, root_storage_dir):
        self.root_dir = root_storage_dir

    def store(self, url, html):
        filename = match('.*/wiki/(.*$)', url).group(1)
        folder = self.root_dir + filename
        filename += '.html'
        if not path.exists(folder):
            makedirs(folder)

        try:
            remove(folder + '/' + filename)
        except:
            pass #Awesome, less work for us

        actual_file = open(folder + '/' + filename, "w")
        actual_file.write(html)
        actual_file.close()
