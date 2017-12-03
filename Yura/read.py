from Yura.endpoint import Endpoint
from Yura.cache import Cache


def read_input():
    V, E, R, C, X = map(int, input().split())

    videos = list(map(int, input().split()))
    endpoints = [Endpoint() for _ in range(E)]
    caches = [Cache(X) for _ in range(C)]

    for i in range(E):
        l, k = map(int, input().split())
        endpoints[i].datacenterdistance = l
        for j in range(k):
            cacheid, l = map(int, input().split())
            endpoints[i].cachesdistance.append((cacheid, l))
            caches[cacheid].endpointsids.append(i)
            caches[cacheid].id = cacheid

    for i in range(R):
        videoid, endpointid, number = map(int, input().split())
        endpoints[endpointid].id = endpointid
        endpoints[endpointid].requests.append((videoid, number))
    # for i in endpoints:
    #     print(i)
    # for i in caches:
    #     print(i)
    return endpoints, caches


"""
for e in endpoints:
    for c in e.cachesdistance:
        cacheid, distance = c[0], c[1]
        caches[cacheid].
"""
read_input()