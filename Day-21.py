# 1799. Maximize Score After N Operations


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        @lru_cache(None)
        def dp(step, mask):
            if mask == (1 << n) - 1:
                return 0

            max_score = 0
            for i in range(n):
                if mask & (1 << i) == 0:
                    for j in range(i + 1, n):
                        if mask & (1 << j) == 0:
                            new_mask = mask | (1 << i) | (1 << j)
                            max_score = max(max_score, step * gcd(nums[i], nums[j]) + dp(step + 1, new_mask))

            return max_score

        n = len(nums)
        return dp(1, 0)
