import networkx as nx
import matplotlib.pyplot as plt

# Define the adjacency list
adjacency_list = {
    "kh": ["tc", "qp", "ub", "ta"],
    "tc": ["kh", "wh", "td", "co"],
    "qp": ["kh", "ub", "td", "wh"],
    "de": ["cg", "co", "ta", "ka"],
    "cg": ["de", "tb", "yn", "aq"],
    "ka": ["co", "tb", "ta", "de"],
    "co": ["ka", "ta", "de", "tc"],
    "yn": ["aq", "cg", "wh", "td"],
    "aq": ["yn", "vc", "cg", "wq"],
    "ub": ["qp", "kh", "wq", "vc"],
    "tb": ["cg", "ka", "wq", "vc"],
    "vc": ["aq", "ub", "wq", "tb"],
    "wh": ["tc", "td", "yn", "qp"],
    "ta": ["co", "ka", "de", "kh"],
    "td": ["tc", "wh", "qp", "yn"],
    "wq": ["tb", "ub", "aq", "vc"]
}

# Create a graph from the adjacency list
graph = nx.Graph(adjacency_list)

# Visualize the graph
plt.figure(figsize=(12, 8))
nx.draw(
    graph, 
    with_labels=True, 
    node_size=800, 
    node_color="lightblue", 
    edge_color="gray", 
    font_size=10
)
plt.title("Graph Visualization", fontsize=16)
plt.show()
