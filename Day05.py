# 839. Similar String Groups

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def is_similar(s1, s2):
            diff = []
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    diff.append(i)
                    if len(diff) > 2:
                        return False
            return len(diff) == 2 and s1[diff[0]] == s2[diff[1]] and s1[diff[1]] == s2[diff[0]]

        n = len(strs)
        similar = {s: set() for s in strs}
        for i in range(n):
            for j in range(i + 1, n):
                if is_similar(strs[i], strs[j]):
                    similar[strs[i]].add(strs[j])
                    similar[strs[j]].add(strs[i])

        visited = set()
        groups = 0
        for s in strs:
            if s in visited:
                continue
            stack = [s]
            visited.add(s)
            while stack:
                cur = stack.pop()
                for nei in similar[cur]:
                    if nei not in visited:
                        stack.append(nei)
                        visited.add(nei)
            groups += 1

        return groups
