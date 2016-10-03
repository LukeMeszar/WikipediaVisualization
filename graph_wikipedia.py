import networkx as nx
import matplotlib.pyplot as plt
import wikipedia as wk
import sys

def main(argv):
    G = nx.DiGraph()
    pos = nx.spring_layout(G)
    pageName = input('Enter wikipedia page: ')
    currentPage = wk.page(pageName)
    title = currentPage.title
    G.add_node(title)
    currentPageLinks = get_links(currentPage)

    for link in currentPageLinks:
        try:
            G.add_node(link)
            G.add_edge(title, link)
            newPage = wk.page(link)
            newPageLinks = get_links(newPage)
            for lnk in newPageLinks:
                G.add_node(lnk)
                G.add_edge(link, lnk)
        except wk.exceptions.DisambiguationError as e:
            print (e.options)


    #print (G.nodes())
    #print (G.edges())
    #nx.draw(G)
    nx.write_graphml(G, 'wiki.graphml')
    #plt.show()

def get_links(page):
    pageLinks = []
    for link in page.links:
        pageLinks.append(link)
    return pageLinks

if __name__ == "__main__":
    main(sys.argv)
