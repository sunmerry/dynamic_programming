from collections import defaultdict
from collections import deque
class Graph:
    def __init__(self,e,n):
        self.graph = defaultdict(list);
        self.nEdges = e
        self.nNodes = n
    def addEdges(self,u,v):
        # for i in range(0,self.nEdges):
        #     u = input("enter edge source: ")
        #     v = input("enter edge destn: ")
        #     print(self.graph)
        self.graph[u].append(v)
    def bfsListing(self,source):
        q = deque()
        visited = [0] * self.nNodes
        q.append(source)
        visited[source]=1
        while q:
            #print("q",q)
            qfront = q.popleft()
            print(qfront)
            #print("nei",self.graph[qfront])
            for node in self.graph[qfront]:
                #print("here",qfront, node)
                if visited[node] == 0:
                    q.append(node)
                    visited[node] = 1
            print(visited)
    def dfsUtil(self,source,visited):

        visited[source] = 1
        print(source)
        for node in self.graph[source]:
            if visited[node] == 0:
                self.dfsUtil(node,visited)

    def dfs(self,source):
        stk = deque()
        stk.append(source)
        visited = [0] * self.nNodes
        visited
        for vertex in self.graph:
            if visited[vertex] == 0:
                self.dfsUtil(vertex,visited)









graph1 = Graph(7,6)
graph1.addEdges(0,1)
graph1.addEdges(0,2)
graph1.addEdges(0,5)
graph1.addEdges(1,3)
graph1.addEdges(2,4)
graph1.addEdges(3,5)
graph1.addEdges(4,5)
source = 0
graph1.bfsListing(source)
graph1.dfs(source)
print(graph1.graph)
