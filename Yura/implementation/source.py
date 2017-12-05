import random

print("Reading")

class Video:
    def __init__(self, iid):
        self.iid = iid
        self.capacity = -1

class Server:
    def __init__(self, iid):
        self.iid = iid
        self.capacity = -1
        self.videos = []
        self.candidates = {}
        self.endpoints = []

class Endpoint:
    def __init__(self, iid):
        self.iid = iid
        self.datacenterdelay = -1
        self.servers = []
        self.requests = []

# ----------------------------
# READING DATA
# ----------------------------

V, E, R, C, X = map(int, input().split())

endpoitslst = [Endpoint(_) for _ in range(E)]
serverlst = [Server(_) for _ in range(C)]
videoslst = [Video(_) for _ in range(V)]

tmp = list(map(int, input().split()))

for i in range(V):videoslst[i].capacity = tmp[i]
for i in range(C):serverlst[i].capacity = X

for e in range(E):
    l, k = map(int, input().split())
    endpoitslst[e].datacenterdelay = l
    for i in range(k):
        c, l = map(int, input().split())
        endpoitslst[e].servers.append((c, l))
        serverlst[c].endpoints.append((e, l))

totalrequestnum = 0

for r in range(R):
    v, e, n = map(int, input().split())
    endpoitslst[e].requests.append((v, n))
    totalrequestnum += n

# ----------------------
# FUNCTIONS
# ----------------------

def find_server(serveriid):
    for item in serverlst:
        if(item.iid == serveriid):
            return item

def fill_server(serveriid):
    # implementing of  particular metrics
    # now it will be num of requests of video
    server = find_server(serveriid)
    for item in server.endpoints:
        endpointid = item[0]
        endpoint = endpoitslst[endpointid]
        for item in endpoint.requests:
            videoid = item[0]
            quantity = item[1]
            server.candidates[videoid] = server.candidates.get(videoid, 0) + quantity

def server_criteria(server):
    # criteria to sort servers
    # now it is time multiplied by requests num
    # sorted by ascending order
    result = 0
    for item in server.endpoints:
        endpointid = item[0]
        latency = item[1]
        requests = 0
        for item in endpoitslst[endpointid].requests:
            requests += item[1]
        result += requests * latency
    return result

def take(serveriid, videoiid):
    server = find_server(serveriid)
    video = videoslst[videoid]
    server.capacity -= video.capacity
    server.videos.append(videoid)

def get_score():
    print("Calculating result")
    saved = 0
    counter = 0
    for endpoint in endpoitslst:
        counter += 1
        percent = counter * 100 / E
        print("Processing : " + str(percent) + "%")
        for item in endpoint.requests:
            videoid = item[0]
            quantity = item[1]
            currentmin = endpoint.datacenterdelay * quantity
            for i in endpoint.servers:
                serveriid = i[0]
                delay = i[1]
                server = find_server(serveriid)
                if(videoid not in server.videos):continue
                currentmin = min(currentmin, quantity * delay)
            saved += endpoint.datacenterdelay * quantity - currentmin
    result = saved * 1000 / totalrequestnum
    return result

def output():
    serverlst.sort(key=lambda n: n.iid)
    print(len(serverlst))
    for item in serverlst:
        print(item.iid, end=' ')
        for v in item.videos:
            print(v, end=' ')
        print()

# -----------------------
# FILLING SERVERS
# -----------------------

for i in range(C):
    fill_server(i)

# -----------------------
# SORTING SERVERS
# -----------------------

serverlst.sort(key=lambda n: server_criteria(n))

# -----------------------
# TAKING VIDEOS
# -----------------------


percent = -1

for c in range(C):
    currentserver = serverlst[c]
    metrics = sorted([(currentserver.candidates[item], item) for item in currentserver.candidates], reverse=True)
    for item in metrics:
        videoid = item[1]
        if(currentserver.capacity < videoslst[videoid].capacity):continue
        take(currentserver.iid, videoid)
        # ----------------------------------------
        # YOU SHOULD RESORT REMAINING SERVERS HERE
        # ----------------------------------------
    percent = (c + 1) * 100 / C
    print("Processing " + str(percent) + "%")

print(get_score())
# output()