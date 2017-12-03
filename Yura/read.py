from Yura.endpoint import Endpoint
from Yura.cache import Cache

V, E, R, C, X = map(int, input().split())

videos = list(map(int,input().split()))
endpoints = [Endpoint() for _ in range(E)]
caches = [Cache(X) for _ in range(C)]

for i in range(E):
    l, k = map(int, input().split())
    endpoints[i].datacenterdistance = l
    for j in range(k):
        cacheid, l = map(int, input().split())
        endpoints[i].cachesdistance.append((cacheid, l))
        caches[cacheid].endpointsids.append(i)

for i in range(R):
    videoid, endpointid, number = map(int, input().split())
    endpoints[endpointid].requests.append((endpointid, number))
"""
for e in endpoints:
    for c in e.cachesdistance:
        cacheid, distance = c[0], c[1]
        caches[cacheid].
"""