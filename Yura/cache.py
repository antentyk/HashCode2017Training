class Cache:
    def __init__(self, capacity):
        self.id = -1
        self.capacity = capacity
        self.endpointsids = []  # id
        self.taken = set()
        self.needs = [{} for _ in range(10000)]

    def __str__(self):
        return """
id: {0}
capacity: {1}
endpointsids: {2}
taken: {3}
needs: {4}

""".format(self.id, self.capacity, self.endpointsids, self.taken, self.needs)
