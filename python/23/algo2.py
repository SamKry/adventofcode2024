import numpy as np
import array
from pprint import pprint
from utils import char2Array
from utils import int2Array

dataFile = "python/23/data.txt"
# dataFile = "python/23/data_small.txt"

"""
example:
kh-ta
co-tc
wh-qp
tb-vc
td-yn
"""


dataArr = char2Array.to2DArray(dataFile, "-")

pprint(dataArr)

adjacency_list = {}

for adj in dataArr:
    if adj[0] not in adjacency_list:
        adjacency_list[adj[0]] = []
    if adj[1] not in adjacency_list[adj[0]]:
        adjacency_list[adj[0]].append(adj[1])
    if adj[1] not in adjacency_list:
        adjacency_list[adj[1]] = []
    if adj[0] not in adjacency_list[adj[1]]:
        adjacency_list[adj[1]].append(adj[0])

pprint(adjacency_list)
# Display the adjacency list
for vertex, neighbors in adjacency_list.items():
    print(f"{vertex} -> {' '.join(map(str, neighbors))}")


def findLargestSet(adjacency_list):
    """
    returns the largest set of vertecies that are ALL connected to EACH OTHER
    """
    largestSet = []
    for vertex, neighbors in adjacency_list.items():
        connected = set(neighbors)
        connected.add(vertex)
        for neighbor in neighbors:
            connected = connected.intersection(adjacency_list[neighbor])
            connected.add(neighbor)
        if len(connected) > len(largestSet):
            largestSet = connected
    return largestSet


largestSet = findLargestSet(adjacency_list)


ans = ",".join(sorted(largestSet))

print("Answer: ", ans)
