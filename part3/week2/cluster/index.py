class FindUnion:
    def __init__(self, numbers):
        self.numbers = numbers
        self.parents = [self.index(n) for n in self.numbers]

    def find(self, x, with_height=False):
        ancestors, height = self.ancestors(x)

        if with_height:
            return ancestors[-1], height
        else:
            return ancestors[-1]

    def union(self, x, y):
        if self.has_same_root(x, y):
            return

        x_root_index, x_height = self.find(x, True)
        y_root_index, y_height = self.find(y, True)

        if x_height < y_height:
            self.parents[y_root_index] = x_root_index
        else:
            self.parents[x_root_index] = y_root_index

    def has_same_root(self, x, y):
        return self.find(x) == self.find(y)

    def ancestors(self, x):  # including itself
        ancestors = [self.parents[self.index(x)]]
        height = 0

        while self.parent_index(x) != self.index(x):
            ancestors.append(self.parent_index(x))
            height += 1

            x = self.numbers[self.parent_index(x)]

        return ancestors, height

    def index(self, x):
        return self.numbers.index(x)

    def parent_index(self, x):
        return self.parents[self.index(x)]


def cluster(edges, size, k):  # edges must be sorted by cost
    data = FindUnion([e for e in range(1, size + 1)])

    count = 0
    i = 0

    while size - count > k - 1:
        while data.has_same_root(edges[i][0], edges[i][1]):
            i += 1

        x = edges[i][0]
        y = edges[i][1]

        data.union(x, y)
        count += 1

    return edges[i][-1]


cluster(sorted(input, key=lambda x: x[-1]), input[0][0], 4)
