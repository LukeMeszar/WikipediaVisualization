import networkx as nx
import matplotlib.pyplot as plt

def main():
    G = nx.Graph()
    h = nx.path_graph(5)
    G.add_nodes_from(h)
    G.add_edges_from(h.edges())

    G.node[0]['name']="panama"

    G.node[1]['name']="costa rica"

    G.node[2]['name']="Argentina"

    G.node[3]['name']="Brazil"

    G.node[4]['name']="Coloumbia"

    G.edge[1][2]['connection']='road'

    nx.write_graphml(G,"te.graphml")

if __name__ == "__main__":
    main()
