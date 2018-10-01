
class FrontierManager(object):

    def __init__(self):
        self.to_visit = []
        self.visited = []
        self.encountered = {}

    def add(self, link, depth, dist_ft):
        try:
            new_depth = min(self.encountered[link][0], depth)
            new_dist_ft = min(self.encountered[link][1], dist_ft)
            self.encountered[link] = (new_depth, new_dist_ft)
        except KeyError:
            self.to_visit.append((link, depth, dist_ft))
            self.encountered[link] = (depth, dist_ft)


    def next(self):
        next_item = self.to_visit[0]
        self.to_visit = self.to_visit[1:]
        self.visited.append(next_item)
        return next_item

    def has_next(self):
        return len(self.to_visit) > 0

    def get_link_journal(self):
        return self.encountered