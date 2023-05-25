# 837. New 21 Game

class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k - 1 + maxPts:
            return 1.0

        result = 0.0
        probabilities = [1.0] + [0] * n  # probabilities[i] := prob to have i points
        windowSum = probabilities[0]  # P(i - 1) + P(i - 2) + ... + P(i - maxPts)

        for i in range(1, n + 1):
            probabilities[i] = windowSum / maxPts
            if i < k:
                windowSum += probabilities[i]
            else:
                result += probabilities[i]
            if i - maxPts >= 0:
                windowSum -= probabilities[i - maxPts]

        return result
