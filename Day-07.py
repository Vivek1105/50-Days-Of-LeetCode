# Problem - 1579. Remove Max Number of Edges to Keep Graph Fully Traversable

class Solution:
    def find(self, i, par):
        if par[i] == -1:
            return i
        par[i] = self.find(par[i], par)  # path compression
        return par[i]
    
    def union_set(self, x, y, par, rnk):
        s1 = self.find(x, par)
        s2 = self.find(y, par)
        
        if s1 != s2:
            # union by rank
            if rnk[s1] > rnk[s2]:
                par[s2] = s1
                rnk[s1] += rnk[s2]
            else:
                par[s1] = s2
                rnk[s2] += rnk[s1]
            return True
        return False
    
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        edges.sort(key=lambda x: x[0], reverse=True)
        # to process the edges of type 3 first, sort the edges vector
        rem = 0
        
        par_alice = [-1] * n
        par_bob = [-1] * n
        rnk_alice = [1] * n
        rnk_bob = [1] * n
        
        for i in range(len(edges)):
            if edges[i][0] == 3:
                fg1 = self.union_set(edges[i][1]-1, edges[i][2]-1, par_alice, rnk_alice)
                fg2 = self.union_set(edges[i][1]-1, edges[i][2]-1, par_bob, rnk_bob)
                if not fg1 and not fg2:
                    # alice and bob are both connected to node x and node y so remove this edge
                    rem += 1
            elif edges[i][0] == 2:
                fg2 = self.union_set(edges[i][1]-1, edges[i][2]-1, par_bob, rnk_bob)
                if not fg2:
                    # bob is connected to node x and node y so remove this edge
                    rem += 1
            else:
                fg1 = self.union_set(edges[i][1]-1, edges[i][2]-1, par_alice, rnk_alice)
                if not fg1:
                    # alice is connected to node x and node y so remove this edge
                    rem += 1
        
        co1, co2 = 0, 0
        for i in range(n):
            if par_alice[i] == -1:
                co1 += 1
            if par_bob[i] == -1:
                co2 += 1
            # if the nodes can be connected, there will be only one parent in the parent array
        
        if co1 == 1 and co2 == 1:
            return rem
        return -1
