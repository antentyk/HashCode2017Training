class Endpoint:
    def __init__(self, cacheslst, requests, datacenterdelay):
        # cacheslst - list of id of caches
        # requests - (video id, number of requests)
        # datacenterdelay - int
        self.caches = set()
        for item in cacheslst:
            self.caches.add(item)
        self.requests = {}
        for item in requests:
            videoid, number = item[0], item[1]
            self.requests[videoid] = number
        self.datacenterdelay = detacenterdelay
