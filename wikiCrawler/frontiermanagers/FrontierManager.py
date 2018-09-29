
class FrontierManager(object):

    def __init__(self):
        self.to_visit = []
        self.visited = []

    def add(self, link, depth):
        for v_link, v_depth in self.visited:
            if v_link == link:
                return
        for tv_link, tv_depth in self.to_visit:
            if tv_link == link:
                return
        self.to_visit.append((link, depth))

    def next(self):
        next_item = self.to_visit[0]
        self.to_visit = self.to_visit[1:]
        self.visited.append(next_item)
        print("Size of todo: " + str(len(self.to_visit)))
        return next_item

    def has_next(self):
        return len(self.to_visit) > 0