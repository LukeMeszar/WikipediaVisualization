import networkx as nx
import matplotlib.pyplot as plt

def main():
    G = nx.Graph()
    G.add_edges_from([(1,2),(1,3),(1,4),(3,4)])
    nx.write_graphml(G, 'so.graphml')

if __name__ == "__main__":
    main()
