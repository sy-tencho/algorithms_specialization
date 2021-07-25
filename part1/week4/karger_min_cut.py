# Runs on Google Colab
import copy
import sys
import random
import gdown


def randomize(graph):
    # 本来2つ目のnodeは一つ目のnodeとは独立して選択されるべき
    key = random.choice(list(graph.keys()))
    value = random.choice(graph[key])

    return key, value


def karger(graph):
    while len(graph) > 2:
        n1, n2 = randomize(graph)

        # node1をnode2に統合する
        graph[n1].extend(graph[n2])

        # node2とのコネクションを持っているnodeがnode1とコネクションを持つように更新
        for n in graph[n2]:
            graph[n].remove(n2)
            graph[n].append(n1)

        while n1 in graph[n1]:
            graph[n1].remove(n1)

        del graph[n2]

    return len(graph[list(graph.keys())[0]])


def main():
    url = 'url to input file'
    file = 'file.txt'
    gdown.download(url, file, quiet=False)

    data = open('file.txt', 'r')

    GRAPH = {}

    for row in data:
        l = [int(s) for s in row.split()]
        GRAPH[l[0]] = l[1:]

    n = len(GRAPH)
    ans = sys.maxsize

    # n回やって全て失敗する確率は1/nなのでn回試行すればほぼ確実に答えが出る
    for _ in range(n):
        graph = copy.deepcopy(GRAPH)
        ans = min([ans, karger(graph)])

    return ans


if __name__ == '__main__':
    main()
