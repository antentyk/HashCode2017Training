class Endpoint:
    def __init__(self):
        self.id = -1
        self.datacenterdistance = -1
        self.cachesdistance = []  # cacheid, int
        self.requests = []  # videoid, int

    def __str__(self):
        return """
id: {3}
dist to datacenter: {0}
dist to caches: {1}
requests: {2}
        """.format(self.datacenterdistance, self.cachesdistance, self.requests, self.id)
