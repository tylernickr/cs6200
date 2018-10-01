
# This class handles merging and ordering importance of links
# Takes in all the links and sorts them during the get method
class LinkJournal(object):

    def __init__(self):
        self.journal = {}

    def add(self, link, depth, dist_ft):
        try:
            new_depth = min(depth, self.journal[link][0])
            new_dist_ft = min(dist_ft, self.journal[link][1])
            self.journal[link] = (new_depth, new_dist_ft)
        except KeyError:
            self.journal[link] = (depth, dist_ft)

    def get_ordered_journal(self):
        results = []
        for key, value in self.journal.items():
            results.append((key, value[0], value[1]))

        results.sort(key=lambda myval: (myval[1] * 1000) + myval[2])
        return results

    def size(self):
        return len(list(self.journal.keys()))
