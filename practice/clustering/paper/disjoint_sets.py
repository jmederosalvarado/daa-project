class DisjointSets:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.counts = [0 for _ in range(n)]
        self.count = n

    def setof(self, item):
        if self.parents[item] != item:
            self.parents[item] = self.setof(self.parents[item])
        return self.parents[item]

    def merge(self, set1, set2):
        root1 = self.setof(set1)
        root2 = self.setof(set2)

        if root1 == root2:
            return False

        if self.counts[root1] < self.counts[root2]:
            root1, root2 = root2, root1

        self.parents[root2] = root1
        self.counts[root1] += self.counts[root2]
        self.count -= 1

        return True
