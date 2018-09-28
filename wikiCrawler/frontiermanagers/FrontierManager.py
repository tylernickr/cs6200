
class FrontierManager(object):

    def __init__(self):
        self.to_visit = []
        self.visited = []

    def add(self, link, depth):
        if (not link in self.to_visit and not link in self.visited):
            self.to_visit.append(link, depth)

    def next(self):
        next_item = self.to_visit[0]
        self.to_visit = self.to_visit[1:]
        return next_item

    def has_next(self):
        return len(self.to_visit) > 0