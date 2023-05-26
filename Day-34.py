class Solution:
    def stoneGameII(self, piles):
        n = len(piles)
        dp = [[0] * n for _ in range(n)]  
        # dp[i][j] := max # of stones Alice can get w/ piles[i:] and M = j
        suffix_sum = piles.copy()

        for i in range(n - 2, -1, -1):
            suffix_sum[i] += suffix_sum[i + 1]

        return self.stoneGameIIHelper(0, 1, dp, suffix_sum)

    def stoneGameIIHelper(self, i, M, dp, suffix_sum):
        if i + 2 * M >= len(dp):
            return suffix_sum[i]
        if dp[i][M] > 0:
            return dp[i][M]

        opponent = suffix_sum[i]

        for X in range(1, 2 * M + 1):
            opponent = min(opponent, self.stoneGameIIHelper(i + X, max(M, X), dp, suffix_sum))

        dp[i][M] = suffix_sum[i] - opponent
        return dp[i][M]
