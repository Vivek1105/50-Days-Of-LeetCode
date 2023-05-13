# 2140. Solving Questions With Brainpower


from typing import List

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)

        for i in reversed(range(n)):
            current_points, current_brainpower = questions[i]
            next_index = i + current_brainpower + 1
            next_points = dp[next_index] if next_index < n else 0
            dp[i] = max(current_points + next_points, dp[i + 1])

        return dp[0]
