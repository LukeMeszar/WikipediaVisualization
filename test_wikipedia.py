import wikipedia as wk
import sys
from random import randint

def main():
    #randomPage = wk.random(1)
    randomPage = "Abstract Algebra"
    print randomPage
    link_traversal(randomPage, 20)


def link_traversal(randomPage, depth):
    if depth <= 0:
        return
    page = wk.page(randomPage)
    pageLinks = []
    for link in page.links:
        pageLinks.append(link)

    randomLink = randint(0,len(pageLinks)-1)
    newLink = pageLinks[randomLink]
    print newLink
    link_traversal(newLink, depth -1)

if __name__ == "__main__":
    main()
