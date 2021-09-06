from networkx.utils import UnionFind

n = 200_000
bits = [int(''.join(bit), 2) for bit in input[1:]]

edges = {}
for i, bit in enumerate(bits):
    if bit in edges:
        edges[bit].append(i)
    else:
        edges[bit] = [i]


masks = [0] * 300
k = 0
for i in range(24):
    for j in range(i, 24):
        mask1 = 1 << i
        mask2 = 1 << j
        masks[k] = mask1 | mask2
        k = k + 1

masks.append(0)


uf = UnionFind(range(n))
keys = edges.keys()
for key in keys:
    for mask in masks:
        neighbor = key ^ mask

        if neighbor in keys:
            nodes = edges[key] + edges[neighbor]
            uf.union(*nodes)


ans = set(uf[x] for x in range(n))
print(len(ans))
