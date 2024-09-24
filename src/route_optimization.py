# src/route_optimization.py
import networkx as nx
import matplotlib.pyplot as plt

def optimize_route():
    G = nx.Graph()
    G.add_edge('Point A', 'Point B', weight=5.5)
    G.add_edge('Point A', 'Point C', weight=8.0)
    G.add_edge('Point B', 'Point C', weight=2.1)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

    shortest_path = nx.dijkstra_path(G, 'Point A', 'Point C', weight='weight')
    print("Shortest Path:", shortest_path)

if __name__ == "__main__":
    optimize_route()
