# Problem - 1416. Restore The Array 

class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        cache = {}
        def backtrack(pos: int) -> int:
            original_pos = pos
            count = 0
            buffer = 0
            if pos in cache:
                return cache[pos]
            for i in range(pos, len(s)):
                buffer *= 10 
                buffer += int(s[i])
                if buffer <= k and i+1 <= len(s)-1 and s[i+1] != '0':
                    count += (backtrack(i+1) % 1000000007)
                if buffer > k:
                    break
            else:
                if buffer <= k:
                    count += 1
            cache[original_pos] = count
            return count
        return backtrack(0) % 1000000007

