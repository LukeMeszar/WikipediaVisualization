import networkx as nx
import matplotlib.pyplot as plt

def main():
    G = nx.Graph()
    G.add_node(1)
    G.add_nodes_from([2,3])

    H = nx.path_graph(10)
    G.add_nodes_from(H)

    G.add_edge(1,2)
    e = (2,3)
    G.add_edge(*e)
    G.add_edges_from([(1,2),(1,3)])
    G.add_edges_from(H.edges())
    #print G.number_of_nodes()
    #print G.number_of_edges()
    #print G.nodes()
    #print G.edges()
    #print G.neighbors(1)

    F = nx.DiGraph(G)
    #print (F.edges)

    FG = nx.Graph()
    FG.add_weighted_edges_from([(1,2,0.125),(1,3,0.75),(2,4,1.2),(3,4,0.375)])
    for n, nbrs in FG.adjacency_iter():
        for nbr, eattr in nbrs.items():
            data = eattr['weight']
            if data < 0.5:
                print ("")
                #print (('%d, %d, %.3f') % (n,nbr,data))

    DG = nx.DiGraph()
    DG.add_weighted_edges_from([(1,2,0.5),(3,1,0.75)])
    #print (DG.out_degree(1, weight = 'weight'))
    #print (DG.successors(1))
    #print (DG.neighbors(1))
    print (G.nodes())
    #nx.draw(G)
    #nx.draw_random(G)
    #nx.draw_circular(G)
    #nx.draw_spectral(G)
    #nx.draw_shell(G)
    #nx.draw_networkx_labels(G)
    plt.show()


if __name__ == "__main__":
    main()
