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


def findTriangles(adjacency_list):
    """
    returns a list of triangles in the graph. it does not contain any duplicates
    """
    triangles = []
    for vertex, neighbors in adjacency_list.items():
        for neighbor in neighbors:
            for neighbor2 in adjacency_list[neighbor]:
                if neighbor2 != vertex and neighbor2 in neighbors:
                    triangle = [vertex, neighbor, neighbor2]
                    triangle.sort()
                    if triangle not in triangles:
                        triangles.append(triangle)
    return triangles


ans = 0

triangles = findTriangles(adjacency_list)

for triangle in triangles:
    for vertex in triangle:
        if vertex.startswith("t"):
            print(f"Found: {triangle}")
            ans += 1
            break

print("Answer: ", ans)
