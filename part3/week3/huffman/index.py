import heapq
import sys


class Tree():
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None


heap = []
for i in input[1:]:
    tree = Tree()
    tree.data = i
    heapq.heappush(heap, (tree.data, tree))


while len(heap) >= 2:
    _, t1 = heapq.heappop(heap)
    _, t2 = heapq.heappop(heap)

    new_tree = Tree()
    new_tree.data = t1.data + t2.data
    new_tree.left = t1
    new_tree.right = t2

    heapq.heappush(heap, (new_tree.data, new_tree))


lengths = []


def count_max(tree, counter):
    if tree.left is None and tree.right is None:
        lengths.append(counter)

    if tree.left:
        count_max(tree.left, counter + 1)

    if tree.right:
        count_max(tree.right, counter + 1)


_, ans_tree = heapq.heappop(heap)
count_max(ans_tree, 0)

lengths = sorted(lengths)
print(lengths[0], lengths[-1])
