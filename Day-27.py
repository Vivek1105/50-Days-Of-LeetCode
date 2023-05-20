# 399. Evaluate Division


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        ans = []
        graph = {}

        # Build the graph
        for i in range(len(equations)):
            A, B = equations[i]
            value = values[i]

            if A not in graph:
                graph[A] = {}
            graph[A][B] = value

            if B not in graph:
                graph[B] = {}
            graph[B][A] = 1 / value

        # Helper function for division
        def divide(A: str, C: str, seen: Set[str]) -> float:
            if A == C:
                return 1.0

            seen.add(A)

            # Value := A / B
            for B, value in graph[A].items():
                if B not in seen:
                    res = divide(B, C, seen)  # B / C
                    if res > 0:  # Valid
                        return value * res  # (A / B) * (B / C) = A / C

            return -1.0  # Invalid

        # Evaluate queries
        for A, C in queries:
            if A not in graph or C not in graph:
                ans.append(-1.0)
            else:
                ans.append(divide(A, C, set()))

        return ans
