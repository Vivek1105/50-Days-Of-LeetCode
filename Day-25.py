# 1557. Minimum Number of Vertices to Reach All Nodes


class Solution:
  def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
    inDegree = [0] * n

    for j, v in edges:
      inDegree[v] += 1

    return [i for i, d in enumerate(inDegree) if d == 0]
