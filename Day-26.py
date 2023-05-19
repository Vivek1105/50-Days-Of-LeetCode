# 785. Is Graph Bipartite?


from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [-1] * n

        def dfs(node, color):
            colors[node] = color

            for neighbor in graph[node]:
                if colors[neighbor] == color:
                    return False

                if colors[neighbor] == -1 and not dfs(neighbor, 1 - color):
                    return False

            return True

        for node in range(n):
            if colors[node] == -1 and not dfs(node, 0):
                return False

        return True
