class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [0]*n

        def dfs(node):
            if node == destination:
                return True
            visited[node] = 1
            for neighbour in adj[node]:
                if visited[neighbour] == 0:
                    if dfs(neighbour):
                        return True
            return False

        return dfs(source)