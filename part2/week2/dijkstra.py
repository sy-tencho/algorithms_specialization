import gdown
import sys


def main():
    url = 'url to file'
    input = 'file.txt'
    gdown.download(url, input, quiet=False)
    data = open('file.txt', 'r')

    GRAPH = {}

    for row in data:
        l = [s for s in row.split()]
        GRAPH[int(l[0])] = [list(map(int, t.split(','))) for t in l[1:]]


def dijkstra(G):
    defined = [1]
    length = {1: 0}

    while len(defined) < len(G.keys()):
        mn = sys.maxsize
        mn_pair = []

        for d in defined:
            if d in G.keys():
                for pair in G[d]:
                    dst = length[d] + pair[1]
                    if dst < mn:
                        mn = dst
                        mn_pair = pair

        defined.append(mn_pair[0])
        length[mn_pair[0]] = mn

        for k in list(G.keys()):
            for p in G[k]:
                if p[0] in defined:
                    G[k].remove(p)

            if G[k] == []:
                del G[k]


if __name__ == '__main__':
    main()
