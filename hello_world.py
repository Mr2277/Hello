class Graph(object):
    def __init__(self, maps):
        self.maps = maps
        self.nodenum = self.get_nodenum()
        self.edgenum = self.get_edgenum()

    def get_nodenum(self):
        return len(self.maps)

    def get_edgenum(self):
        count = 0
        for i in range(self.nodenum):
            for j in range(i):
                if self.maps[i][j] > 0:
                    count += 1
        return count

    def insert_node(self):
        for i in range(len(self.maps)):
            self.maps[i].append(-1)
        self.maps.append([-1] * (self.nodenum) + [0])
        self.nodenum += 1

    def insert_edge(self, x, y, weight):
        if x < 0 or x >= self.nodenum or y < 0 or y > self.nodenum or weight <= 0 or x == y:
            return
        else:
            self.maps[x][y] = self.maps[y][x] = weight
            self.edgenum += 1

    def breath_first_search(self):
        queue = []
        visited = [False] * self.nodenum
        res = []

        def bfs():
            while len(queue) > 0:
                i = queue.pop(0)
                for j in range(self.nodenum):
                    if self.maps[i][j] > 0 and visited[j] == False:
                        res.append(j)
                        visited[j] = True
                        queue.append(j)

        if self.nodenum <= 0:
            return res
        else:
            queue.append(0)  # index, value
            visited[0] = True
            res.append(0)
            bfs()

        for i in range(self.nodenum):
            if visited[i] == False:
                res.append(i)
                visited[i] = True
                queue.append(i)
                bfs()

        return res

    def depth_first_search(self):
        res = []
        visited = [False] * self.nodenum

        def dfs(i):
            res.append(i)
            visited[i] = True
            for j in range(self.nodenum):
                if self.maps[i][j] > 0 and visited[j] == False:
                    dfs(j)

        if self.nodenum > 0:
            dfs(0)
        for i in range(self.nodenum):
            if visited[i] == False:
                dfs(i)
        return res


maps = [[0, 3, 9, -1], [3, 0, -1, 5], [9, -1, 0, -1], [-1, 5, -1, 0]]
graph = Graph(maps)
print('邻接矩阵为\n%s' % graph.maps)
print('节点数据为%d，边数为%d\n' % (graph.nodenum, graph.edgenum))
graph.insert_node()
print('-------插入一个节点--------')
print('邻接矩阵为%s' % graph.maps)
print('节点数据为%d，边数为%d\n' % (graph.nodenum, graph.edgenum))
graph.insert_edge(0, 4, 7)
print('-------插入一个边--------')
print('邻接矩阵为%s' % graph.maps)
print('节点数据为%d，边数为%d\n' % (graph.nodenum, graph.edgenum))
print('-------广度优先遍历--------')
print(graph.breath_first_search())
print('-------深度优先遍历--------')
print(graph.depth_first_search())
