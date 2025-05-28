from collections import deque

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        m = len(edges1) + 1 # get the number of nodes in tree 1
        n = len(edges2) + 1 # get the number of nodes in tree 2
    
        # We will want to build adjaceny lists for tree 1
        adj1 = [[] for _ in range(m)]
        for u, v in edges1:
            adj1[u].append(v)
            adj1[v].append(u)
        

        # Then build adjacency trees in tree 2

        adj2 = [[] for _ in range(n)]
        for u, v in edges2:
            adj2[u].append(v)
            adj2[v].append(u)

        # Preprocess to find best node to jump to from tree 1 to tree 2
        best = 0
        for i in range(n):
            connections = self.bfs((i, adj2, k - 1))
            best = max(best, connections)
    
        # Finally we can build our result array
        res = []
        for i in range(m):
            connections = self.bfs(i, adj1, k)
            res.append(connections + best)
        
        return res
    
    
    # Need to study BFS more, definitely a weak point for me right now.
    def bfs(self, start, adj, k):
        q = deque()
        q.append((start, -1))
        count = 0

        while q and k >= 0:
            size = len(q)
            count += size
            for _ in range(size):
                u, parent  = q.popleft()
                for v in adj[u]:
                    if v != parent:
                        q.append((v, u))
            k -= 1
        return count
