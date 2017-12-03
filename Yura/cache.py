class Cache:
    def __init__(self ,capacity):
        self.capacity = capacity
        self.endpointsids = [] # id
        self.taken = set()
        self.needs = [{} for _ in range(10000)]