# problem - 1697. Checking Existence of Edge Length Limited Paths



class Solution:
    def distanceLimitedPathsExist(self, num_nodes: int, edges: List[List[int]], queries: List[List[int]]) -> List[bool]:
        parents = [i for i in range(num_nodes)]

        def find(vert):  
            if parents[vert] == vert:
                return vert
            parents[vert] = find(parents[vert])
            return parents[vert]

        def union(vert1, vert2):  
            vert1 = find(vert1)
            vert2 = find(vert2)
            parents[vert1] = vert2

        edges.sort(key=lambda x: x[2])
        for i in range(len(queries)):
            queries[i].append(i)
        queries.sort(key=lambda x: x[2])
        i = 0
        results = [False for j in range(len(queries))]
        for query in queries:
            limit = query[2]
            while i < len(edges) and edges[i][2] < limit:
                u = edges[i][0]
                v = edges[i][1]
                union(u, v)
                i += 1
            p = query[0]
            q = query[1]
            query_index = query[3]
            if find(p) == find(q):
                results[query_index] = True
        return results
