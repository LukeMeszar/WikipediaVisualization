import networkx as nx
import matplotlib.pyplot as plt

def main():
    G = nx.cubical_graph()
    pos = nx.spring_layout(G)

    nx.draw_networkx_nodes(G, pos,
                            nodelist=[0,1,2,3],
                            node_color='r',
                            node_size=500,
                            alpha =0.8)
    nx.draw_networkx_nodes(G, pos,
                            nodelist=[4,5,6,7],
                            node_color='b',
                            node_size=500,
                            alpha=0.8)

    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
    nx.draw_networkx_edges(G, pos,
                            edgelist=[(0,1),(1,2),(2,3),(3,0)],
                            width=8, alpha=0.5, edge_color='b')

    labels={}
    labels[0]=r'$a$'
    labels[1]=r'$b$'
    labels[2]=r'$c$'
    labels[3]=r'$d$'
    labels[4]=r'$\alpha$'
    labels[5]=r'$\beta$'
    labels[6]=r'$\gamma$'
    labels[7]=r'$\delta$'
    nx.draw_networkx_labels(G, pos,labels,font_size=16)
    nx.write_graphml(G, 'ex.graphml')
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    main()
