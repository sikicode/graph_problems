class Graph:
    def __init__(self, n):
        self.root = [_ for _ in range(n)]
        self.n = n

    """O(1) find"""
    def find(self, x):
        return self.root[x]

    """Assume x is the new root"""
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        for i in range(self.n):
            if self.root[i] == rootY:
                self.root[i] = rootX

    def connected(self, x, y):
        return self.root[x] == self.root[y]

if __name__ == '__main__':
    gh = Graph(4)
    gh.union(1, 2)  # 0 1-2 3 [0,1,1,3]
    gh.union(1, 3)  # 0 3-1-2 [0,1,1,1]
    print(gh.find(3))  # 1
    print(gh.root)
    print(gh.connected(0, 3))  # False
