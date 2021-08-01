import requests
import sys
import threading

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)

url = 'url to file'
r = requests.get(url, allow_redirects=True)

open('file.txt', 'wb').write(r.content)

num_nodes = 875715

GRAPH = [[] for _ in range(num_nodes)]
GRAPH_REV = [[] for _ in range(num_nodes)]

seen1 = [False] * num_nodes
seen2 = [False] * num_nodes
scc = [0] * num_nodes

order = []

file = open('file.txt', 'r')
data = file.readlines()

cnt = 0

for line in data:
    items = line.split()
    GRAPH[int(items[0])].append(int(items[1]))
    GRAPH_REV[int(items[1])].append(int(items[0]))


def dfs1(s):
    if seen1[s]:
        return

    seen1[s] = True

    for v in GRAPH_REV[s]:
        if not seen1[v]:
            dfs1(v)

    order.append(s)


def dfs2(s):
    global cnt

    if seen2[s]:
        return

    seen2[s] = True
    cnt += 1

    for v in GRAPH[s]:
        if not seen2[v]:
            dfs2(v)


def kosaraju():
    for i in range(1, num_nodes):
        if not seen1[i]:
            dfs1(i)

    order.reverse()

    for node in order:
        global cnt
        cnt = 0
        dfs2(node)
        scc[node] = cnt

    scc.sort(reverse=True)
    print(scc[:5])


thread = threading.Thread(target=kosaraju)
thread.start()
