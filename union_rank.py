class FindUnion:
    def __init__(self, n):
        self.root = [_ for _ in range(n)]
        self.rank = [1] * n
        self.size = n
    def find(self, x):
        while self.root[x] != x:
            x = self.root[x]
        return x
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootY != rootX:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1
    def connected(self, x, y):
        return self.find(x) == self.find(y)